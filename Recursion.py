
import sys

print(sys.setrecursionlimit(2000))
print(sys.getrecursionlimit())

i = 0
def greet():
    global i
    i +=1
    print("Hello world", i)
    greet()

greet()