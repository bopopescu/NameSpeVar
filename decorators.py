# In decorators, functions are passed as an argument into another function
# and then called inside the wrapper function. It is also called as "meta programming"
# where a part of the program attempts to change another part of program at compile time

def div(x,y):
    z = x/y
    return z

result = div(2,4)
print ("%.2f" % result)

def smart_deco(func):
    def inner_div(a,b):
        if a<b:
            a,b = b,a
        return func (a,b)
    return inner_div

div = smart_deco(div)
result1 = div(2,4)
print (result1)

