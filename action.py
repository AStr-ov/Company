from innit import *

def show(name):
    with open(file,'r') as d:
        tmp = ''
        for i in d:
            tmp += i
        [print(i)for i in tmp.split('==========')if name in i]

def add(t1,t2,t3,t4,t5):
    with open(file,'a')as d:
        d.write(f'\nName: {input(t1)}\nTeam: {input(t2)}\nPost: {input(t3)}\nSalary: {input(t4)}\nPhone: {input(t5)}\n')
        d.write('==========\n')

def dell(nam):
    tmp = ''
    with open(file,'r')as d:
        for i in d:
            tmp += i
    with open(file,'w')as d:
        for i in tmp.split('=========='):
            if nam not in i:
                d.write(i)
                d.write('==========\n')
