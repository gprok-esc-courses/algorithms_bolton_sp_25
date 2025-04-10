from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread 

client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 8070))

def server_thread(server):
    while True:
        msg_bytes = server.recv(1024)
        msg = msg_bytes.decode('utf-8')
        print(msg)

name = input("Give name: ")

th = Thread(target=server_thread, args=(client,))
th.start()

while True:
    msg = input("Give message: ")
    msg_bytes = str.encode(name + ": " + msg)
    client.send(msg_bytes)