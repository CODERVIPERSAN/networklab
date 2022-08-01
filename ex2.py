
from socket import socket ,AF_INET,SOCK_STREAM

with socket(AF_INET,SOCK_STREAM) as client:
    server_address = "www.google.com"
    client.connect((server_address,80))
    client.sendall(b"GET/HTTP/1.1\r\nHost:www.google.com\r\nAccept:text/html\r\n\r\n")

    print(str(client.recv(4096),'utf-8'))
