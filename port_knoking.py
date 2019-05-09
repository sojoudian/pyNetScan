import socket
s = socket.socket()
s.settimeout(2)
t = socket.socket()

host = input("Host is :")
port = input("Port number to scan is :")

try:
    s.connect((host, int(port)))
    r = s.recv(1024)
    next_port = int(r[24:29])
    print("Connecting to port", next_port)
    t.connect((host, next_port))
    print(t.recv(1024))
    s.close()
except socket.error as error:
    print(error)
