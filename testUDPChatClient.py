import socket
import threading,time
import re

def udpLink(sock,addr):
    while True:
        time.sleep(0.1)
        print(sock.recv(1024).decode('utf-8'))

print('input your sever ip:')
while True:
    ip = input()
    if re.match(r'\d{3}.\d{3}.\d{1}.\d{3}',ip):
        break
    print('unlawful IP')
print('input your name:')
name = input()
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(bytes(name+':'+'online',encoding = 'utf-8'),(ip,9999))
t = threading.Thread(target = udpLink,args=(s,(ip,9999)))
t.start()
while True:
    data = input()
    s.sendto(bytes(name+':'+data,encoding = 'utf-8'),(ip,9999))
s.close()
