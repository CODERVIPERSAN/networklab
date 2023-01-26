from socket import socket,AF_INET,SOCK_STREAM
server_address =('localhost',1025)

if __name__=="__main__":
    with socket(AF_INET,SOCK_STREAM) as client:
        client.connect(server_address)
        
        with open("c"+client.recv(1000).decode(),"w") as file:
            data = client.recv(1000).decode()
            file.write(data)


    