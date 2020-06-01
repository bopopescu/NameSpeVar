from numpy import *

arr1 = array([
             [10,20,30,40],
             [90,60,40,30]
             ])
print(arr1)

m = matrix(arr1)
print(arr1)

m1 = matrix('10,20,30; 40,50,60; 70,80,90')
print(m1)


m2 = matrix('1,2,3; 4,5,6; 7,8,9')

m3 = m1 + m2
print (m3)

m3 = m1 * m3
print (m3)


m2 = matrix('1,2,3; 4,5,6; 7,8,9')

m4 = matrix('1,1; 2,2; 3,3')

m5 = m2 * m4

print("multiply :", m5)

print("*******manual multiplication*******")

m2 = matrix('1,2,3; 4,5,6; 7,8,9')

m4 = matrix('1,1; 2,2; 3,3')
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[1, 1, 1],
     [2, 2, 2],
     [3, 3, 3]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows of X
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)

print("___________________________")

a1 = array([2,5,1,4,3,3])
a1 = a1.reshape(3,2)
a2 = array([8,1,5,3,5,2,1,7])
a2 = a2.reshape(2,4)
m1 = matrix(a1)
m2 = matrix(a2)
m3 = m1 * m2
print(m3)