from socket import socket ,AF_INET,SOCK_STREAM

s= socket(AF_INET,SOCK_STREAM)

s.connect(("www.google.com",80))
s.sendall(b"GET/HTTP/1.1\r\nHost:www.google.com\r\nAccept:text/html\r\n\r\n")

print(str(s.recv(4096),'utf-8'))
