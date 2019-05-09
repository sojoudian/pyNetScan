import socket
s = socket.socket()
s.settimeout(2)

host = input("Host is :")
port = 80

s.connect((host, int(port)))

req = 'HEAD / HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'


print("Sending :")
print(req)
s.send(req.encode())

print("Received: ")
response = s.recv(1024)
UTF_encoded_data = response.decode('utf-8')
print("decoded", UTF_encoded_data)

s.close()


