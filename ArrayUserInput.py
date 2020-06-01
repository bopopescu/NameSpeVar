
from array import *

n = int(input("enter array length: "))
Arr = array('i',[])

for p in range(n):
    p = int(input("Enter next value: "))
    Arr.append(p)
print(Arr)

q = int(input("value to be searched :"))

k=0
for a in Arr:
    if a == q:
        print (k)
        break
    else:
        k+=1

print(Arr.index(q))









