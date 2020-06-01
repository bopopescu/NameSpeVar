
def greet(): # this is how function is defined
    print("Welcome to functions")

greet()    # this is how function is called


def add_sub(x,y): # function with result statement
    c = (x+y)
    d = (x-y)
    return c,d

result1,result2 = add_sub(9,4)
print(result1, result2)

def mul(x,y): # function with result statement
    c = (x*y)
    return c

result3=mul(4,6)
print(result3)

# Function Arguments

# Immutable object as argument - Integer
def update(x):
    x = 4
    print("x : ", x)
    print("memory location : ", id(x))

a=10
update(a)
print("a : ", a)
print("memory location : ", id(a))

def update(lst):
    print("lst : ", lst)
    print("memory location1 : ", id(lst))
    lst[1] = 50
    print("lst : ", lst)
    print("memory location2 : ", id(lst))

lst = [10,20,30]
print("lst : ", lst)
print("memory location3 : ", id(lst))
update(lst)
print("lst : ", lst)
print("memory location4 : ", id(lst))

def update(p):
    print("p : ", p)
    print("memory location of p : ", id(p))
    p[1]= q

p = [1, 2, 3]
q = 9
update(p)
print("p updated : ", p)
print("memory location of p updated : ", id(p))

