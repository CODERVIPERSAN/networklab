
from socket import socket,AF_INET,SOCK_STREAM

server_address = ('localhost',1028)
print(__name__)
if __name__=="__main__":
    with socket(AF_INET,SOCK_STREAM) as client:
        client.connect(server_address)
        client.sendall(input("type some message ").encode())
        print("Echo:",client.recv(1000).decode())




    

