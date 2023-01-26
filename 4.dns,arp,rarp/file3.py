from socket import socket,AF_INET,SOCK_STREAM

ip_address=('localhost',1040)

with socket(AF_INET,SOCK_STREAM) as client:
    value = input("type message=")
    client.connect(ip_address)
    client.sendall(value.encode())
    print("Echo:",client.recv(4096).decode())