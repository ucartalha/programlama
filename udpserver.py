import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# this might be database or a file
di = {'talha': '1234'}

while (True):
    # receiving name from client
    name, addr1 = UDPServerSocket.recvfrom(bufferSize)

    # receiving pwd from client
    pwd, addr1 = UDPServerSocket.recvfrom(bufferSize)

    name = name.decode()
    pwd = pwd.decode()
    msg = ''
    if name not in di:
        msg = 'name does not exists'
        flag = 0
    for i in di:
        if i == name:
            if di[i] == pwd:
                msg = "pwd match"
                flag = 1
            else:
                msg = "pwd wrong"
        bytesToSend = str.encode(msg)
        # sending encoded status of name and pwd
        UDPServerSocket.sendto(bytesToSend, addr1)