import socket

port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_addr = input("Server IP Address : ")

if ip_addr == "":
    ip_addr = 'localhost'

addr = (ip_addr, port)

while True:
    msg = input("<- ")
    sock.sendto(msg.encode(), addr)
    print("-> ", end='')
    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())