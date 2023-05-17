import socket
import threading
import time

HOST = "localhost"
PORT = 8080


def connect_to_client(conn, addr):
    print("Connection has established")
    data = conn.recv(1024)
    conn.sendall(b"Thanks for interaction with me!")
    time.sleep(5)
    print(f"Data from Addr: {data}, {addr}")
    conn.close()


print("Starting the server....")
s_sock = socket.socket()

s_sock.bind((HOST, PORT))

s_sock.listen()

print(f"Server is listening on {PORT}")

while True:
    # returns a new socket object and the address info
    conn, addr = s_sock.accept()
    t = threading.Thread(target=connect_to_client, args=(conn, addr))
    t.start()

#  s_sock.close()
