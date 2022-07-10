import socket 
import time
import random
from _thread import *

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 1027
counter = 0

try:
    serverSocket.bind((ip,port))  
except socket.error as e:
    print(e)
serverSocket.listen()
print("listening...")

def threadConnection(connection, num):
    time.sleep(random.uniform(1,5))
    filename = connection.recv(1024).decode()
    connection.send("Filename delivered".encode())
    print("Filename recieved from client " + str(num))
    file = open(filename + str(num) + ".txt", 'w')
    
    data = connection.recv(1024).decode()
    connection.send("Data delivered".encode())
    print("Data recieved from client " + str(num))
    file.write(data)
    file.close()
    connection.close()

while 1:
    (connection, address) = serverSocket.accept()
    counter += 1
    print("client " + str(counter) + " is connected")
    start_new_thread(threadConnection, (connection, counter))

serverSocket.close()