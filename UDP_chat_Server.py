import socket

port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

print("Wating for client")
while True:
    print("상대방 : ", end = '')
    data , addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())

    resp = input("나윤주 : ")
    sock.sendto(resp.encode(),addr)