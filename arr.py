from array import *

arr=array('i',[2,4,5,6,7,8,7,6,4])
print(arr)

#using for loop (square of arr numbers)
narr=array(arr.typecode,(a*a for a in arr))
print('narr = ',narr)
print()

#using while loop
i=0
while i<len(narr):
    print(narr[i],'',end='')
    i+=1

print()
print()

for i in range(len(arr)):
    print(arr[i],'',end='')

print()
print()

for e in arr:
    print(e)

print()

print(arr.buffer_info())
print()

arr.reverse()
print(arr)
print()

#string

st=array('u',['a','b','c'])

print(st)