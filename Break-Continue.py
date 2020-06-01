print ("---Break---")
av = 5

x = int(input("How many candy's you want?"))

i =1

while i <=x:
    if x >av:
        print ("out of stock")
        break
    else:
        print("Candy")
        i+=1
print("Bye now")

print ("---Continue---")

for y in range (1,15):
    if y%2!=0 or y%4!=0:
        continue

    print(y)
print("Done")

print ("---pass is to ignore the condition---")


for z in range (15,1,-1):
    if z%2!=0:
        pass
    else:
        print(z)
print("Done")