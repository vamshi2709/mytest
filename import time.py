import time


def add1(a, b):
    return a+b

def add(*args):
    print(args)
    sum = 0
    for i in args:
        sum = sum + i
    return sum

def names(**kargs):
    name = kargs.get('name', 'default')
    return name
    
names(name ='Yeshwanth', test = 123)

names()

# a = add(1,2)
# b = add(2,3,4,5,6,7)

print(a,b)