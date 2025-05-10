import socket

# Sunucunun IP adresi ve portu
server_ip = '127.0.0.1'
server_port = 8881

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((server_ip, server_port))


message = "Why don't you call me any more?\r\n"
sock.send(message.encode())


response_data = sock.recv(1024)
print(f"Sunucudan gelen cevap: {response_data.decode()}")


sock.close()
