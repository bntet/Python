#1
class Animal:
    name= None
    def call(self):
        print('动物在叫')
class Dog(Animal):
    def call(self):
        print('汪汪')
class Cat(Animal):
    def call(self):
        print('喵喵')
Dog().call()
Cat().call()

#2
def fun(i):
    if i==1 or i==2:
        return 1
    else:
        return fun(i-1)+fun(i-2)

for x in range(1,11):
    if fun(x)>10:
        break
    else:
        print(fun(x))

#3
s = [i for i in range(100) if i%2==1]
print(s)


#4
def add(x,y):
    try:
        return x+y
    except BaseException as e:
        print(e)
print(add(1,''))
print(add(1,2))
print('----------------------------')

def sub(x,y):
    try:
        return x-y
    except BaseException as e:
        print(e)
print(sub(1,""))
print(sub(2,1))
print('----------------------------')

def mul(x,y):
    try:
        return x*y
    except BaseException as e:
        print(e)
print(mul(2,1))
print('----------------------------')

def div(x,y):
    try:
        return x/y
    except BaseException as e:
        print(e)
print(div(1,0))
print(div(4,2))

