# -*- coding: utf-8 -*-
# 导入socket库:
import socket
import threading
import time
import sys
host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
sock,addr = s.accept()
print('Connection built')
info = sock.recv(1024).decode()
while info != 'exit':
  print('Mary:'+info)
  send_mes = input()
  sock.send(send_mes.encode())
  if send_mes =='exit':
    break
  info = sock.recv(1024).decode()
sock.close()
s.close()
 
