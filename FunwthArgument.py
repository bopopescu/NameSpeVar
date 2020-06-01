def Add(a,b=0):
    c=a+b
    return c

result=Add(9)
print("result :", result)
print("++++++++++++++++++++++")

result=Add(9, 8)
print("result :", result)
print("======================")
def Sum(a,*b):
    c = a
    for i in b:
        c = c + i
    return c

e = Sum(2,3,4,5,6)
print ("result :", e)