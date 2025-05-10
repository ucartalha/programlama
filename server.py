import socket

host = '127.0.0.1'
port = 8881

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((host, port))

sock.listen(5)

print(f"Sunucu {host}:{port} üzerinde çalışıyor...")

try:
    while 1:
        newSocket, address = sock.accept()
        print(f"Bağlantı kuruldu: {address}")


        while 1:
            receivedData = newSocket.recv(1024)
            if not receivedData:
                break

            newSocket.send(receivedData)


        newSocket.close()
        print(f"Bağlantı kapandı: {address}")

finally:

    sock.close()
