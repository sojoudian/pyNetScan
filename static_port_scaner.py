import socket

s = socket.socket()
s.settimeout(2)
host = input("Host is :")
port = input("Port number to scan is :")

try:
    s.connect((host, int(port)))
    print(s.recv(1024))
    s.close()
except socket.error as error:
    print(error)
