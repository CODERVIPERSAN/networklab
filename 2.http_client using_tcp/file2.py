from socket import socket,AF_INET,SOCK_STREAM

#create socket
with socket(AF_INET,SOCK_STREAM) as client :
    serveradd = "www.google.com"
    #connect
    client.connect((serveradd,80))
    #send 
    client.sendall(b"GET/HTTP/1.1\r\nHost:www.google.com\r\nAccept:text/html\r\n\r\n")
    
    #receive
    print(str(client.recv(4096),'utf-8'))

#close