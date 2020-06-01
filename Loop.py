print ("****************************Simple while*************************************")
i = 5
P = "Pallavi"
while i>=1:
    print ("Pallavi", i)
    i= i-1

print ("****************************Double while*************************************")

a = 5

while a>=1:
    print("Pallavi", end="")
    b = 1
    while b<=4:
        print (" learn python", end="")
        b=b+1
    a=a-1
    print()

print ("*****************************For loop*******************************")

x = [10,20,63.5,'pallavi',1,5]

for i in x:
    print(i)

print ("--------------------------")

a='Pallavi'

for p in a:
    print(p)

print ("--------------------------")

for b in [1,2,3,4,'pallavi',3.47]:
    print(b)

print ("*******************range in for*************************************")

for c in range(10):
    print (c)
print ("--------------------------")


for d in range(0, 21, 4):
    print (d)
print ("--------------------------")


for e in range(5, 0, -1):
    print (e)
print ("--------------------------")

for f in range(10,1 ,-1):
     if f%5!=0:
       print (f," , ", end="")

     else:
       print (f, " : not matching cond"," , ", end="")

print ("--------------------------")

