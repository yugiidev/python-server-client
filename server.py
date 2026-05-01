import socket

def start_server():
  host = "127.0.0.1"
  port = 5500

  sv_socket = socket.socket()
  sv_socket.bind((host, port)) 
  sv_socket.listen(1)

  connection, address = sv_socket.accept()
  print("Connection from: " + str(address))
  while True: 
    data = connection.recv(1024).decode()
    if not data:
      break
    print("From connected user: " + str(data))
    data = input(' > ')
    connection.send(data.encode())

  connection.close()
  
if __name__ == '__main__':
  start_server()