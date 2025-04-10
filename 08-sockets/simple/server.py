from socket import socket, AF_INET, SOCK_STREAM

server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 8070))

server.listen()
print("Server started on port 8070")

while True:
    conn, addr = server.accept()
    print(conn, addr)
    msg_bytes = conn.recv(1024)
    msg = msg_bytes.decode('utf-8')
    print(msg)

    
