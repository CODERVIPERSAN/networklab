from socket import socket,AF_INET,SOCK_STREAM

ip_address=('localhost',1043)

with socket(AF_INET,SOCK_STREAM) as server:
    server.bind(ip_address)
    server.listen(1)
    # data_dict ={"1.1.1.1":"MAC1","2.2.2.2":"MAC2"}
    while True:
        # print("loading ...")
        connection,connectedto = server.accept()
        # print(f"connection established to{connectedto}")
        data = connection.recv(4096).decode()
        print("client:",data)
        if(data=="exit"):
            connection.sendall("terminated".encode())
            break
        else:
            response = input("you:")
            connection.sendall(response.encode())

    connection.close()