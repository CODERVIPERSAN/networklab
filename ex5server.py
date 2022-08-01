from ex5 import server_address,socket,AF_INET,SOCK_STREAM

with socket(AF_INET,SOCK_STREAM) as server:
    server.bind(server_address)
    server.listen(1)
    connection,client_address = server.accept()
    file_name=input("enter the file name")+".txt"
    connection.sendall(file_name.encode())
    with open ("s"+file_name,"a") as file:
        with open("s"+file_name,"r") as file:
            data = file.read()
            connection.sendall(data.encode())
            connection.close()