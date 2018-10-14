#1
def do(fun):
    def wrapper(*args):
        if type(*args) is str and str(*args).islower():
            print("是字符串")
            print(str(*args).upper())
        else:
            print("不是字符串")
            func(*args)
    return wrapper
@do
def func(stri):
    print(stri)
func("safasf2~")

#2

#3

#4
f = (i for i in range(50) if i%2==0)
for i in f:
    print(i)

#5
import os
def do(path):
    for i in os.listdir(path):
        yield i
d = do('D:/')
for i in d:
    print(i)
