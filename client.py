import socket

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
 
  message = input(" > ")
  
  while message.lower().strip() != 'logout':
    try:
      cl_socket.sendall(message.encode())
      data = cl_socket.recv(1024).decode()
      if not data:
        print("Connection closed by server.")
        break
      print(f"Received from server: {data}")
      message = input(" > ")
    except Exception as e:
      print(f"Connection with server lost. An error occurred: {e}")
      break

  cl_socket.close()

if __name__ == '__main__':
  start_client()