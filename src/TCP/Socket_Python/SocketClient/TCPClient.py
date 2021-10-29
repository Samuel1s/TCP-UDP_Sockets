from socket import *

host = 'localhost'
port = 55551

cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))

while True:
    msg = input("Digite: ")
    cli.send(msg.encode())