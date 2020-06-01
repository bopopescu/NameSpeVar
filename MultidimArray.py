from numpy import *

Arr = array([
            [10,20,30,40,25,35],
            [60,70,80,90,33,12],
            [20,40,60,80,22,67]
            ])
print(Arr)

print(Arr.dtype)

print(Arr.ndim)

print(Arr.shape)

print(Arr.size)

Arr1 = Arr.flatten()
print("2 to 1 dim conversion - Arr1 is 1 dim : ", Arr1)

Arr2 = Arr.reshape(6,3)
print("changing shape of Arr : ", Arr2)

Arr3 = Arr.reshape(3,2,3)
print("changing shape of Arr : ", Arr3)
