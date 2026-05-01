import socket

def start_client():
  host = "127.0.0.1"
  port = 5500

  cl_socket = socket.socket()

  try:
    cl_socket.connect((host, port))
    print("Connected to server at " + host + ":" + str(port))
  except:
    print("Connection to server failed.")
    return
 
  message = input(" > ")
  
  while message.lower().strip() != 'logout':
    cl_socket.send(message.encode())
    data = cl_socket.recv(1024).decode()
    print("Received from server: " + data)
    message = input(" > ")

  cl_socket.close()

if __name__ == '__main__':
  start_client()