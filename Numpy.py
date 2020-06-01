from numpy import *

arr = array([1,2,3,4],int)
print(arr)

arr1 = array([1,2,3,4])
print(arr1)

print("++++2 DIM ARRAY+++++")

e  = array([(10,20,30), (40,50,60)])
print(e)

arr1 = array([1,2,3,4.2,5])
print(arr1.dtype)
print(arr1)

print("++++++++++++")

arr =  linspace(1,10,5)
print(arr)
arr =  linspace(1,10)
print(arr)

print("++++++++++++")

arr =  logspace(1,10,6,endpoint=3)
print("logspace :", arr)

print('%.2f' %arr[4])
print("++++++++++++")

arr =  arange(10,20,2)
print(arr)

print("++++++++++++")

arr =  zeros(5)
print(arr)

print("++++++++++++")
arr =  ones(4)
print(arr)

print("++++++++++++")
print("=======#add 5 to all members in array========")

arr = arr + 5
print(arr)

print("=======#add 2 arrays ========")

arr1 = array([10,20,30,40,50])
arr2 = array([50,40,30,20,10])

arr3 = arr1 + arr2
print(arr3)


print("================")

print("sin: ", sin(arr1))

print("cos: ",cos(arr1))

print("log: ",log(arr1))

print("sqrt: ",sqrt(arr1))

print("sort: ",sort(arr1))

print("sum: ",sum(arr1))

print("min: ",min(arr1))

print("max: ",max(arr1))

print("nonzero: ",count_nonzero(arr1))

print("concatenate: ",concatenate([arr1,arr2]))

print("*********Array copy*********")

print("shallow or simple copy")  #B = array([3,4,6,8,2,5])

A = array([2,5,7,9,1,3])
B = A
print(B)
print(id(A))
print(id(B))

print("creating Alias or shallow copy")

#after creating alias change value in A, it will still change value in B i.e. shallow copy
B = A.view()
A[1] = 10
print(A)
print(B)
print(id(A))
print(id(B))

print("DEEP copy")

B = A.copy()
A[2] = 25
print(A)
print(B)
print(id(A))
print(id(B))
