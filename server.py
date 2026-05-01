import socket
import threading

def start_server():
  host = "127.0.0.1"
  port = 5500

  sv_socket = socket.socket()
  sv_socket.bind((host, port)) 
  sv_socket.listen()

  while True: 
    connection, address = sv_socket.accept()
    print("Connection from: " + str(address))

    thread = threading.Thread(target=handle_client, args=(connection, address))
    thread.start()
    print("Active connections: " + str(threading.active_count() - 1))
   
  
def handle_client(connection, address):
  while True:
    try:
      data = connection.recv(1024).decode()
      if not data:
        break
      print("Received from " + str(address) + ": " + data)
      connection.send((data).encode())
    except:
      print("Connection with " + str(address) + " closed.")
      break
  connection.close()

if __name__ == '__main__':
  start_server()