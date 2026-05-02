import socket
import json

def start_client():
  host = "127.0.0.1"
  port = 5500

  cl_socket = socket.socket()

  try:
    cl_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")
  except:
    print("Connection to server failed.")
    return

  try:
    message = input(" > ")
    while message.lower().strip() != 'logout':
      if message.strip() == "":
        print("Please enter a valid message.")
        message = input(" > ")
        continue
      try:
        package_send = {
          "content": message
        }
        json_message = json.dumps(package_send)
        cl_socket.sendall(json_message.encode())
        data = cl_socket.recv(1024).decode()
        if not data:
          print("Connection closed by server.")
          break
        package_response = json.loads(data)
        print(package_response['content'])
        message = input(" > ")
      except Exception as e:
        print(f"Connection with server lost. An error occurred: {e}")
        break
  except KeyboardInterrupt:
    print("\nClient is shutting down.")
    cl_socket.close()

if __name__ == '__main__':
  start_client()