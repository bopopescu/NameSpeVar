    #import array as Arr - Arr is alias


## signed is positive and negative value and unsigned is only positive value
##'b' = signed char; 'B' = unsigned char // python type = int
#'h' = signed short; 'H' = unsigned short // python type = int
#'i' = signed int; 'I' = unsigned int // python type = int
#'l' = signed long; 'L' = unsigned Long // python type = int
#'f' = float; 'd' = double // python type = float
#'u' = py_UNICODE // python type = Unicode character

from array import *

Index = array('i',[5,1, 3, 6, 7, 10])

print (Index)

print(Index.buffer_info()) # to print array location and size

Index.append(4)
Index.reverse()

Index.count(5)

print(Index)

print(len(Index))

for e in range(len(Index)):
    print (Index[e])

add = sum(Index)
print (add)

print("===============")
#sum of all values in array without using Sum function
total = 0
for a in Index:
    total += a
print (total)

print("===============")

#Move array values to new array

NewArr = array(Index.typecode,[a for a in Index])

for z in NewArr:
    print(z)
print("===============")


