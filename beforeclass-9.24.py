#1
import random
def fun():
    listpass = []
    num = int(input('请输入长度:'))
    type = input('请输入类型，例如：大写字母：uc,小写字母：lc,数字：num,特殊字符：oth:')
    other = ('~','#','!','@','$','%','^','&','*','(',')')
    for i in range(num):
        if type == 'uc':
            upass = chr(random.randint(65,90))
            listpass.append(upass)
            upass_res = ''.join(listpass)
        if type == 'lc':
            upass = chr(random.randint(97,122))
            listpass.append(upass)
            upass_res = ''.join(listpass)
        if type == 'num':
            upass = chr(random.randint(48,57))
            listpass.append(upass)
            upass_res = ''.join(listpass)
        if type == 'oth':
            upass = random.choice(other)
            listpass.append(upass)
            upass_res = ''.join(listpass)
    return upass_res
print(fun())





#2
def fun(zlis,znum):
    flag = 0
    if znum not in zlis:
        print('no f')
        return
    if len(zlis)%2 == 0:
        for i in zlis:
            if i == znum:
                flag = zlis.index(i)+1
                break
        if flag <= (len(zlis)/2):
            print('left')
        else:
            print('right')
    if len(zlis)%2 == 1:
        for i in zlis:
            if i == znum:
                flag = zlis.index(i)+1
                break
        if flag < int(len(zlis)/2)+1:
            print('left')
        elif flag > int(len(zlis)/2)+1:
            print('right')
        else:
            print('conter')
fun([1,2,3,4],4)


#3
def sfilter():
    num = []
    for i in range(2,101):
        for j in range(2,i):
            if i%j == 1:
                break
            else:
                num.append(i)
                break
    print(num)
sfilter()


#4

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

#5
def fun(zlis):
    zmin = 0
    for i in zlis:
        if i<=zmin:
            zmin = i
    return zmin
print(fun([1,2,-1,6,5,9,74,-1]))
