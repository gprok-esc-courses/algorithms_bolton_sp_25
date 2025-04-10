from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def client_thread(con, clist):
    while True:
        msg_bytes = con.recv(1024)
        msg = msg_bytes.decode('utf-8')
        print(msg)
        for c in clist:
            c.send(msg_bytes)

clients = []

server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 8070))

server.listen()
print("Server started on port 8070")

while True:
    conn, addr = server.accept()
    print(conn, addr)
    clients.append(conn)
    th = Thread(target=client_thread, args=(conn, clients))
    th.start()
    

    
