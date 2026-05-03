import socket
import json
import logging

def start_client():
  host = "127.0.0.1"
  port = 5500

  cl_socket = socket.socket()

  logging.basicConfig(
    filename='client.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
  )

  try:
    cl_socket.connect((host, port))
    logging.info(f"Connected to server at {host}:{port}")
  except:
    logging.error("Connection to server failed.")
    return

  try:
    username = input("Enter your username: ").strip()
    while not username:
      logging.info("Username cannot be empty. Please enter a valid username.")
      username = input("Enter your username: ").strip()
    message = input(" > ")
    while message.lower().strip() != 'logout':
      if message.strip() == "":
        logging.info("Please enter a valid message.")
        message = input(" > ")
        continue
      try:
        package_send = {
          "user": username,
          "content": message
        }
        json_message = json.dumps(package_send)
        cl_socket.sendall(json_message.encode())
        data = cl_socket.recv(1024).decode()
        if not data:
          logging.info("Connection closed by server.")
          print("Connection closed by server.")
          break
        package_response = json.loads(data)
        logging.info(package_response['content'])
        message = input(" > ")
      except Exception as e:
        logging.error(f"Connection with server lost. An error occurred: {e}")
        break
  except KeyboardInterrupt:
    logging.info("\nClient is shutting down.")
    cl_socket.close()

if __name__ == '__main__':
  start_client()