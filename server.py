import json
import socket
import threading
import logging

import os
from dotenv import load_dotenv

load_dotenv()

def start_server():
  host = "0.0.0.0"
  port = int(os.getenv("port"))

  sv_socket = socket.socket()
  sv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sv_socket.bind((host, port)) 
  sv_socket.listen()

  logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
  )

  blocked_ips = ["192.168.1.100"]  # Example of blocked IPs

  try:
    while True: 
      connection, address = sv_socket.accept()

      if address[0] in blocked_ips:
        logging.info(f"Blocked connection attempt from: {address}")
        connection.close()
        continue

      logging.info(f"Connection from: {address}")

      thread = threading.Thread(target=handle_client, args=(connection, address))
      thread.daemon = True
      thread.start()
      logging.info(f"Active connections: {threading.active_count() - 1}")
  except KeyboardInterrupt:
    logging.info("\nServer is shutting down.")
    sv_socket.close()

def handle_client(connection, address):
  while True:
    try:
      data = connection.recv(1024).decode()
      if not data:
        break
      package_received = json.loads(data)
      logging.info(f"{package_received['user']}: {package_received['content']}")
      print(f"{package_received['user']}: {package_received['content']}")
      package_response = {
        "content": f"Server received your message: {package_received['content']}"
      }
      json_response = json.dumps(package_response)
      connection.sendall(json_response.encode())
    except Exception as e:
      logging.error(f"Connection with {address} closed due to error: {e}")
      break
  connection.close()

if __name__ == '__main__':
  start_server()