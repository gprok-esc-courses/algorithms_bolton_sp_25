from socket import socket, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 8070))

msg = input("Give message: ")
msg_bytes = str.encode(msg)
client.send(msg_bytes)
print("DONE")