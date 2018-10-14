#1
from functools import partial
def mul(a,b):
    return a*b
par_add = partial(mul,2)
print(par_add(10))

#2
from functools import partial
def add01(a,b,c):
    return a+b+c
par_add02 = partial(add01,2)
par_add03 = partial(par_add02,3)
print(par_add03(10))

#3
import datetime
def time(func):
    def wrapper(*args,**kw):
        star_time = datetime.datetime.now()
        func()
        over_time = datetime.datetime.now()
        print(f'需要时间{(over_time-star_time).total_seconds()}')
    return wrapper
@time
def demo():
    for i in range(10000):
        print(i)
demo()

#4
def test(func):
    def wrapper(*args,**kw):
        try:
            func(*args,**kw)
        except ZeroDivisionError:
            print("除数不能为0")
        else:
            return func(*args,**kw)
    return wrapper

@test
def div(a,b):
    print(a/b)
div(1,0)

#5
import datetime
def do(fun):
    def wrapper(*args,**kw):
        fun()

        print("Done")
        print(datetime.datetime.now())
    return wrapper

@do
def func():
    print('Hello World')

func()
