#Chat messenger client 
import socket 
import select 
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
userName = input("What is your username? ")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
clientSocket.connect((IP, PORT)) 
clientSocket.setblocking(False)

username = userName.encode('utf-8') 
userNameHeader = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
clientSocket.send(userNameHeader + username)

while True:
    message = input(f"{userName} > ")
    if message:
        message = message.encode('utf-8')
        messageHeader = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        clientSocket.send(messageHeader + message.encode('utf-8'))

    try: 
        while True:
            userNameHeader = clientSocket.recv(HEADER_LENGTH)
            if not len(userNameHeader):
                print("Connection closed by the server")
                sys.exit()

            userNameLength = int(userNameHeader.decode('utf-8').strip())
            userName = clientSocket.recv(userNameLength).decode('utf-8')

            messageHeader = clientSocket.recv(HEADER_LENGTH)
            messageLength = int(messageHeader.decode('utf-8').strip())
            message = clientSocket.recv(messageLength).decode('utf-8')

            print(f"{userName} > {message}")

    except IOError as e: 
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print(f'Reading erroe: {str(e)}')
            sys.exit()
        continue 

    except Exception as e: 
        print(f'Reading error: {str(e)}')
        sys.exit()

