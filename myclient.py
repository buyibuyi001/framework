import socket

ip_port = ('192.168.7.11', 9999)
sk = socket.socket()
sk.connect(ip_port)
sk.sendall('haha douyu\n')
sk.sendall('you like join this\n')
server_reply = sk.recv(1024)
# server_reply_three = sk.recv(1024)
print server_reply
# print server_reply_three
# sk.sendall('join this\n')
# server_reply_two = sk.recv(1024)
# print server_reply_two
sk.close()
