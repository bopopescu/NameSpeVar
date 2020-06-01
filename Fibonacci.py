
n=int(input("Enter upper range: "))


def fib():
    lst = []
    if n < 0:
        print("Please enter positive value")
        lst.append("Please enter positive value")
    else:
        a = 0
        b = 1
        lst.append(a)
        lst.append(b)
        for num in range (n+1):
            c = a + b
            a = b
            b = c
            lst.append(c)
     #      if len(lst)>=10:  to limit number of values to be printed
     #           break
    return lst

Series = fib()

print ("Series : ", Series)

print("****************** Only to print last value from series **************************")

n=int(input("Enter upper range: "))

def fib1():
    lst1=[]
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    lst1.append(c)
    return lst1

series1 = fib1()
print ("Series1 : ", series1)