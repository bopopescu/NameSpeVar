x,y = 20, 30

x = (x+y)
y = (x-y)
x = (x-y)

print (x, y)

x,y = y,x

print (x, y)

temp = x

x = y
y = temp

print (x, y)

x = x ^ y
y = x ^ y
x = x ^ y

print (x, y)

print ("*****************************************************************")

x = int(input(" enter 1st value"))
y = int(input(" enter 2nd value"))
print(type(x))

z = x+y
print(z)

print ("*****************************************************************")

ch = input("Enter a Char")
print(ch)

ch = input("Enter a Char")[0]
print(ch)


print ("*****************************************************************")

Result = eval(input("Enter an expression"))
print(Result)

print ("*****************************************************************")

import sys
x=int(sys.argv[0])
y=int(sys.argv[0])
z = x-y
print(z)


print ("*****************************************************************")
