import socket

host = input("Host is :")
port = int(input("Port number to scan is :"))

for port in range(port):
    try:
        s = socket.socket()
        s.settimeout(2)
        print(port)
        s.connect((host, port))
        print("connected", s.recv(1024))
        s.close()
    except socket.error as error:
        print(error)