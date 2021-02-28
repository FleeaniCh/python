from socket import *
from time import sleep

sockfd = socket()
server_addr = ('192.168.0.199',8888)
sockfd.connect(server_addr)

while True:
    sleep(0.3)
    sockfd.send(b'msg')

