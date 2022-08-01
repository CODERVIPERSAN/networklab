from socket import socket,AF_INET,SOCK_STREAM
from ex3 import server_address
with socket(AF_INET,SOCK_STREAM) as server:
    server.bind(server_address)
    server.listen(1)
    print("Waiting for the connection")
    connection,client_address=server.accept()
    print(f"connection is done with{client_address}")
    data = connection.recv(1000)
    print("recieved",data)
    connection.sendall(data)
    