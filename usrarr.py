from array import *

arr=array('i',[])

n=int(input('Enter the length : '))

for i in range(n):
    x=int(input('Enter the val : '))
    arr.append(x)

print(arr)

s=int(input('Enter the val for search : '))
k=0
for e in arr:
    if e==s :
        print('s = ',k)
        break
    k+=1

print('arr= ',arr.index(s))