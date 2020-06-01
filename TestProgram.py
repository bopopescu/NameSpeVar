
for a in range(4):
    for b in range(4):
        print("#", end="")
    print()

print("------------------------------")

for p in range(4):
    for q in range(4-p):
        print("#", end="")
    print()

print("------------------------------")

for i in range(4):
    for j in range(i + 1):
        print("#", end="")
    print()

print("------------------------------")

tuple1 = (10, 20, 30, 40, 50, 60)
print(tuple1)
count = 0
for i in tuple1:
    print("tuple1[%d] = %d"%(count, i));