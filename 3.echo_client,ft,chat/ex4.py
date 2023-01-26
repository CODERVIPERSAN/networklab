# client program
from socket import socket,AF_INET,SOCK_STREAM

server_address=('localhost',1031)

if __name__=="__main__":
    with socket(AF_INET,SOCK_STREAM) as client:
        client.connect(server_address)
        message = input()
        client.sendall(message.encode())
        while message!="end":
            data = client.recv(1000).decode()
            if data =="end":
                break
            if data:
                print(data)
                message =input()
                client.sendall(message.encode())
            else:
                break
        





