#1
def fun(name,age):
    print(f'{name}在{2018+100-age}年为100岁')
fun('xuzhiqian',17)


#2
def fun():
    n = int(input("请输入整数"))
    if n%2 == 0:
        print('偶数')
    elif n%2 ==1:
        print('奇数')
    else:
        print('请输入整数')
fun()

#3
def fun(ls):
    flag = 0
    for i in ls:
        if i=='':
            flag = 0
        else:
            flag = 1
    if flag:
        print('没空')
    else:
        print('有空')
fun([1,2,''])

#3.2
def fun(ls):
    while '' in ls:
        print('有空')
        break

fun([1,2])

#3.3
def fun(ls):
    return all(ls)

print(fun([1,2,'']))

#4.1
def fun(ls):
    return [x*x for x in ls]
x = fun([1,2,3])
print(x)

#4.2
def fun(ls):
    return map(lambda x: x*x,ls)
x = list(fun([1,2,3]))
print(x)

#5
from functools import reduce
def fun(ls):
    return reduce(lambda x,y: x+y,ls)
x = fun([1,2,3])
print(x)

#6
def fun(ls):
    return [x**0.5 for x in ls]
x = fun([4,16,64])
print(x)

#7
def fun(lst,lst2):
    st = set(lst)
    st2 = set(lst2)
    ls = []
    for i in st:
        for j in st2:
            if i == j:
                ls.append(j)
    return ls
x = fun([4,16,64,1,64],[1,64,4])
print(x)

#8.1
def fun(a,b,c):
    if a>b:
        b = a
    if b>c:
        c = b
    return c
x = fun(100,50,101)
print(x)

#8.2
def fun(a,b,c):
    max = 0
    if a>b:
        max = a
    else:
        max = b
    if c>max:
        max = c
    return max
x = fun(100,50,101)
print(x)
