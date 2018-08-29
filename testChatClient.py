# -*- coding: utf-8 -*-
# 导入socket库:
import socket
import threading
import time
import sys
s= socket.socket()
host = socket.gethostname()
print("connection to " + host + ":")
port = 12345
s.connect((host,port))
print('Linked')
info = ''
while info != 'exit':
  print('Jack:'+info)
  send_mes=input()
  s.send(send_mes.encode())
  if send_mes =='exit':
    break
  info = s.recv(1024).decode()
s.close()
