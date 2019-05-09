import socket

s = socket.socket()
s.settimeout(2)

port = input("Port number to scan is :")

try:
    s.connect(("boshra.com", int(port)))
    print(s.recv(1024))
    s.close()
except socket.error as error:
    print(error)