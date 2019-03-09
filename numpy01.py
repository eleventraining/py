from builtins import print

from numpy import *

#creating array using array() function
arr=array([1,2,3,4,5],int)

print(arr)

print(arr.dtype)
print()
#creating array using llinspace() function
arr1=linspace(0,15,16)

print('arr1 : ',arr1)
print('arr1.dtype : ',arr1.dtype)
print()
#
arr2=arange(1,15,2)

print('arr2 : ',arr2)
print()
#
arr3=logspace(1,40,5)

print('arr3[0] : ',arr3[0])
print()
#

arr4=zeros(5)
print('arr4 : ',arr4)
print()
#
arr5=ones(5,int)
print('arr5 : ',arr5)
print()