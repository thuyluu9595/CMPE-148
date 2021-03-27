# import socket module
from socket import *
import sys  # In order to terminate the program

serverHost = '192.168.1.35'
serverPort = 1234
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        print("about to receive data")
        message = connectionSocket.recv(1024)
        print("received ", message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        print("outputdata", outputdata)
        # Send one HTTP header line into socket
        connectionSocket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n")
        connectionSocket.send(b"\r\n")
        print("sent HTTP/1.x 200 OK")
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError as e:
        print("IOE exception ", e)
        # Send response message for file not found
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n")
        connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        # Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data


