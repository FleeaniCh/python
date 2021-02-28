from socket import *
from second_step.io_linux.exec_read_word import search_word

sockfd = socket(AF_INET,SOCK_DGRAM)
server_addr = ('192.168.0.199',8887)
sockfd.bind(server_addr)

while True:
    word,addr = sockfd.recvfrom(1024)
    # 查单词
    data = search_word(word.decode())
    sockfd.sendto(data.encode(),addr)