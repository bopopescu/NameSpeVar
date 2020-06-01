

a= 10
print(id(a))
b= 16

def argument():
#    global a - this global will not let you override the value outside function, hence use globals()
    a= 20
    x= globals()['a']
    print("x: ", x) # will have same addr as global a
    print(id(x))

    print("inside arg: ", a)

    globals()['a'] = 25
    print("a: ", a)
    print(id(a))

argument()

print("outside arg: ", a)

