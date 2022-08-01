#  server 
from ex4 import server_address,socket,SOCK_STREAM,AF_INET

with socket(AF_INET,SOCK_STREAM) as server:
    server.bind(server_address)
    server.listen(1)
    print("waiting for connection")
    connection,client_address = server.accept()
    while True:
        data = connection.recv(1000).decode()
        if(data=="end"):
            break
        if data :
            print(data)
            message=input()
            connection.sendall(message.encode())
        else:
            break
    connection.close()

