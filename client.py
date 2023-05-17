import socket
# Server's address
HOST = "localhost"
PORT = 8080
c_sock = socket.socket()

c_sock.connect((HOST, PORT))

c_sock.sendall(b"Hello World!")
data = c_sock.recv(1024)

print(f"Data received at client side: {data}")

c_sock.close()

