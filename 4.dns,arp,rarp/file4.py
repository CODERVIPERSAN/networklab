from socket import socket,AF_INET,SOCK_STREAM

ip_address=('localhost',1043)

with socket(AF_INET,SOCK_STREAM) as client:
    client.connect(ip_address)
    value = input("you:")
        
    client.sendall(value.encode())
    while True:
        chat = client.recv(4096).decode()
        if(chat=="exit"):
            break
        else:
            print(f"server:{chat}")
            value = input("you:")
            client.sendall(value.encode())