import socket 

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 1027

clientSocket.connect((ip,port))
print("connected")

clientSocket.send("file".encode())
msg = clientSocket.recv(1024).decode()
print(msg)

file = open("data/file.txt", 'r')
data = file.read()
clientSocket.send(data.encode())
msg = clientSocket.recv(1024).decode()
print(msg)

file.close()
clientSocket.close()