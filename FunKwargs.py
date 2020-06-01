#keyworded, variable-length argument list
#**kwargs

def person(name, **data):
    print (name)
    for i, j in data.items():
        print(i,j)

person('Pallavi', age = 34, City = 'Thane', Country = 'India')
