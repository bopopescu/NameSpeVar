
fun = lambda a:a*a
result = fun(5)
print(result)


fun = lambda a,b:a+b
result = fun(5,6)
print(result)

### with and without using lambda function or expression

#Find even without lamba


def is_even(n):
    return n%2==0

def is_double(n):
    return n*2

num = [3, 5, 4, 7, 6, 9, 8]

even = list(filter(is_even,num))

print("without Lambda :",even)

even = list(filter(lambda n:n%2==0,num)) # separate def of is_even fun not required

print("with Lambda :",even)

double = list(map(is_double,even))

print("without Lambda :",double)

double = list(map(lambda n:n*2,even))

print("with Lambda :",double)

from functools import reduce

def add_all(a,b):
    return (a+b)

Addition = reduce(add_all,double)

print("without Lambda :",Addition)

Addition = reduce(lambda a,b:a+b,double)

print("without Lambda :",Addition)