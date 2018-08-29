###Filename:zip.py
##import os
##import time 
##source = [r'C:\Users\jaydean\Desktop\testZip\1', r'C:\Users\jaydean\Desktop\testZip\2']
##target_dir = r'C:\Users\jaydean\Desktop\testZip'
##target = target_dir  + os.sep +  time.strftime('%Y%m%d%H%M%S') + '.zip'
##zip_command = "zip -qr %s %s" % (target, ' '.join(source))
##print (zip_command)
##if os.system(zip_command) == 0:
##    print ('Successful backup to', target)
##else:
##    print ('Backup FAILED' )
###End of:zip.py

###Filename:class.py
##class Person:
##    '''Represents a person.'''
##    popul = 0
##    def __init__(self,name):
##        self.name = name   
##        #print('class var is %s'%self.name)
##    def sayHi(self):
##        print('my name is %s' % self.name)
##        Person.popul = Person.popul+1
##    def delN(self):
##        Person.popul -= 1
##    def howMany(self):
##        print('now people is %s' % Person.popul)
##a = Person('haha')
##a.sayHi()
##a.howMany()
##b = Person('heihei')
##b.sayHi()
##b.delN()
##b.howMany()
##
###End of:class.py

###Filename:extend.py
##class schoolMem:
##    def __init__(self,name,age):
##        self.name = name
##        self.age = age
##    def tellMsg(self):
##        print('mem name is %s and mem is %s years old' % (self.name,self.age))
##
##class stuMem(schoolMem):
##    def __init__(self,name,age,fee):
##        schoolMem.__init__(self,name,age)
##        self.fee = fee
##    def tellMsg(self):
##        schoolMem.tellMsg(self)
##        print('stu fee is %s yuan' % self.fee)
##class teacherMem(schoolMem):
##    def __init__(self,name,age,sala):
##        schoolMem.__init__(self,name,age)
##        self.sala = sala
##    def tellMsg(self):
##        schoolMem.tellMsg(self)
##        print('teacher salary is %s yuan' % self.sala)
##class foreignStuMem(stuMem):
##    def __init__(self,name,age,fee,cost):
##        stuMem.__init__(self,name,age,fee)
##        self.cost = cost
##    def tellMsg(self):
##        stuMem.tellMsg(self)
##        print('foreign stu cost is %s yuan' % self.cost)        
##a = stuMem('haha','23','6000')
##a.tellMsg()
##
##b = teacherMem('haobin','55','7000')
##b.tellMsg()
##
##c = foreignStuMem('haobin','24','7000','20000')
##c.tellMsg()
##
##
###End of:extend.py

###Filename:ioFile.py
##poem = '''my life is brilliant
##my love is pure
##i saw an angle
##'''
##f = open('1.txt','w')
##f.write(poem)
##f.close()
##f = open('1.txt')
##while True:
##    line = f.readline()
##    if(len(line) == 0):
##        break
##    else:
##        print(line,end=' ')
###End of:ioFile.py

###Filename:pickle.py
##import pickle as p
##fileList = ['hah','ww','qq']
##f = open('2.pickle','wb')
##p.dump(fileList,f)
##f.close()
##del fileList
##with open('2.pickle','rb') as f:
##    stored = p.load(f)
##print (stored)
###End of:pickle.py

###Filename:exception.py
##class myException(Exception):
##    def __init__(self,length,atleast):
##        Exception.__init__(self)
##        self.length = length
##        self.atleast = atleast    
##try:
##    a = input('please input a word:')
##    if(len(a)<3):
##        print('in')
##        raise myException(len(a),3)
##except EOFError:
##    print('this is a eof exception')
##except myException as e:
##    print('the word length is %s ,but we need %s'% (e.length,e.atleast) )
##else:
##    print('fine')
###End of:exception.py

###Filename:exceptionFinally.py
##import time   
##try:
##    a = open('1.txt','r')
##    while True:
##        b= a.readline()
##        if len(b) == 0:
##            break
##        else:
##            print(b)
##            time.sleep(2)
##except EOFError:
##    print('this is a eof exception')
##finally:
##    a.close()
##    print('closed')
###End of:exceptionFinally.py

###Filename:sysMod.py
##import sys
##def readFile(fileName):
##    f = open(fileName)
##    while True:
##        a = f.readline()
##        if len(a) == 0:
##            break
##        else:
##            print(a)
##if len(sys.argv) < 2:
##    print('lack argument')
##if sys.argv[1].startswith('-'):
##    opt = sys.argv[1][1:]
##    if opt == 'h':
##        print('this is help')
##    elif opt == 'v':
##        print('the version is 3.7')
##    else:
##        print('invalid parameter')
##    sys.exit()        
##else:
##    '''
##    this need cmd window or linux terminal
##    '''
##    print(sys.version)
##    g = readFile(sys.argv[1])
##    print(g)
###End of:sysMod.py

###Filename:sysMod.py
####listOne = [1,2,3]
####listTwo = [2*i for i in listOne if i > 2]
####print(listTwo)
##def fun(** arg):
##    
##    '''
##    test this is docstring
##    '''
##    print('ok')
##    print(arg)
##    
##fun(name='aaa',name2='bbb')
##print(fun.__doc__)
###End of:sysMod.py

###Filename:GUI.py
##import tkinter as tk
##import random
##window = tk.Tk()
##window.title('my window')
##window.geometry('200x400')
##var = tk.StringVar()    
##l = tk.Label(window, 
##textvariable=var,   
##bg='green', font=('Arial', 12), width=15, height=2)
##l.pack()
##def hit_me():
##    global on_hit
##    if on_hit == False:     
##        on_hit = True
##        var.set('you hit me')   
##    else:       
##        on_hit = False
##        var.set('') 
##b = tk.Button(window, 
##    text='hit me',      
##    width=15, height=2,
##    command=hit_me )    
##b.pack()    
##on_hit = False  
##
##
##e = tk.Entry(window,show=' ')
##e.pack()
##c = tk.Button(window, activebackground='red',bd=4,
##    text='hit me',      
##    width=15, height=2,
##    command=hit_me )    
##c.pack()
###End of:GUI.py

###Filename:RE.py
###INFO:test verbose RE ,re.research()
##import re
##s = '100 NORTH BROAD MAIN ROAD'
##p = re.sub('ROAD$','RD.',s)
##p2 = s[:-4]+s[-4:].replace('ROAD','RD.')
##p3 = s.replace('ROAD','RD.')
##p4 = re.sub('\\bROAD$','RD.',s)
##pattern='''
##        ^            #beginning of string
##        M{0,3}$
##        '''
##print(re.search(pattern,'M',re.VERBOSE))
###End of:RE.py

###Filename:RE for Roman Number.py
###INFO:test RE Roman Number
###-*- coding: utf-32 -*
##'''
##使用编码UTF-32确保在函数info_()中的注释
##__doc__显示正确
##'''
##import re
##pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
###'use {0,3}to change as:^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$' 
##print(re.search(pattern,'MDLV'))
###MDLV means year 1555
##def info_doc():
##    """
##    when using info_doc.__doc__:
##    I=1
##    V=5
##    X=10
##    L=50
##    C=100
##    D=500
##    M=1000
##    (1)基本数字Ⅰ、X 、C 中的任何一个，自身连用构成数目，或者放在大数的右边连用构成数目，都不能超过三个；放在大数的左边只能用一个。
##    (2)不能把基本数字 V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；放在大数的右边采用相加的方式构成数目，只能使用一个。
##    (3)V 和 X 左边的小数字只能用Ⅰ。
##    (4)L 和 C 左边的小数字只能用×。
##    (5)D 和 M 左 边的小数字只能用 C 。
##    """
##    print('ok!info above!')
###End of:RE for Roman Number.py

###Filename:multiprocesing.py
##from multiprocessing import Process
##import os
### 子进程要执行的代码 需要在linux环境运行或者cmd窗口，否则不显示子进程运行的函数
##def run_proc(name):
##    print('Run child process %s (%s)...' % (name, os.getpid()))
##def run_proc2(name):
##    print('Run child2 process %s (%s)...' % (name, os.getpid()))
##if __name__=='__main__':
##    print('Parent process %s.' % os.getpid())
##    p = Process(target=run_proc, args=('test',))
##    p2 = Process(target=run_proc2, args=('test2',))
##    print('Child process will start.')
##    p.start()
##    p.join()
##    print('=========================')
##    p2.start()
##    p2.join()
##    print('Child process end.')
###End of:multiprocesing.py

###Filename:multiprocesing.py
##from multiprocessing import Pool
##import os, time, random
##
##def long_time_task(name):
##    print('Run task %s (%s)...' % (name, os.getpid()))
##    start = time.time()
##    time.sleep(random.random() * 3)
##    end = time.time()
##    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
##
##if __name__=='__main__':
##    print('Parent process %s.' % os.getpid())
##    p = Pool(4)
##    for i in range(5):
##        p.apply_async(long_time_task, args=(i,))
##    print('Waiting for all subprocesses done...')
##    p.close()
##    p.join()
##    print('All subprocesses done.')
###End of:multiprocesing.py

###Filename:test generator
###Intro:obj c ->produce->send none->yield->n=1->print,send 1->consumer->print 200k
##def consumer():
##    r = ''
##    while True:
##        n = yield r
##        if not n:
##            return
##        print('[CONSUMER] Consuming %s...' % n)
##        r = '200 OK'
## 
##def produce(c):
##    c.send(None)
##    n = 0
##    while n < 5:
##        n = n + 1
##        print('[PRODUCER] Producing %s...' % n)
##        r = c.send(n)
##        print('[PRODUCER] Consumer return: %s' % r)
##    c.close()
## 
##c = consumer()
##produce(c)
###End of File:test generator


####Filename:test decorator
##import time
## 
##def deco(func):
##    def wrapper():
##        startTime = time.time()
##        func()
##        endTime = time.time()
##        msecs = (endTime - startTime)*1000
##        print("time is %d ms" %msecs)
##    return wrapper
## 
##@deco
##def func():
##    print("hello")
##    time.sleep(1)
##    print("world")
## 
##f = func #这里f被赋值为func，执行f()就是执行func()
##f()
#####End of File:test decorator


##Filename:test matplot start
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(1000)
##y = np.random.standard_normal(10)
y = np.random.standard_normal((100,2))
print ("y = %s"% y)
z = range(len(y))
#plt.xlim( 0,10)
plt.grid(True)

plt.hist(y,bins = 100,label = ['1st','2st'],color=['b','r'],stacked=True)
plt.legend(loc = 0)

plt.bar(width=0.8)
plt.show()













##Filename:test matplot  end


