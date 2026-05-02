import socket
import threading

def start_server():
  host = "127.0.0.1"
  port = 5500

  sv_socket = socket.socket()
  sv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  sv_socket.bind((host, port)) 
  sv_socket.listen()

  blocked_ips = ["192.168.1.100"]  # Example of blocked IPs

  try:
    while True: 
      connection, address = sv_socket.accept()

      if address[0] in blocked_ips:
        print(f"Blocked connection attempt from: {address}")
        connection.close()
        continue

      print(f"Connection from: {address}")

      thread = threading.Thread(target=handle_client, args=(connection, address))
      thread.start()
      print(f"Active connections: {threading.active_count() - 1}")
  except KeyboardInterrupt:
    print("\nServer is shutting down.")
    sv_socket.close()

def handle_client(connection, address):
  while True:
    try:
      data = connection.recv(1024).decode()
      if not data:
        break
      print(f"Received from {address}: {data}")
      connection.sendall((data).encode())
    except:
      print(f"Connection with {address} closed.")
      break
  connection.close()

if __name__ == '__main__':
  start_server()