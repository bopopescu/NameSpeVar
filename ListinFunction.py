
# to accept list values as user input
lst = []
j = int(input("Enter number of value in the list :"))
for i in range(j):
    p = int(input("Enter values one by one :"))
    lst.append(p)
print(lst)

# define function to count # of Odd and Even from the list

def count():
    even = 0
    odd = 0
    a = lst
    for i in a:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return (even, odd)

even , odd = count()

print(even, odd)

print("Even # : {} and Odd # : {}".format(even,odd))


print("________________________________________________________")

names = []
n = int(input("Enter # of names to be entered :"))
for i in range(n):
    p=str(input("Enter a name :"))
    names.append(p)
print(names)

def countChar():
    Char = 0
    for i in names:
        print ("name :", i)
        for j in range(len(i)):
            print("index :", j)
            if j > 3:
                Char+=1
        print(Char)
    return Char

Char=countChar()

print(Char)
print("Name with more than 4 Char : {}".format(countChar()))

# easier way of doing same thing

def countCh():
    Ch = 0
    for i in names:
        if len(i) > 3:
            Ch += 1
    return Ch

Ch=countCh()

print(Ch)
print("Name with more than 4 Char : {}".format(Ch))
