from numpy import *

#add 5 to every element in an array
arr=array([1,2,3,4,5])

arr=arr + 5

print(arr)
print()

#
ar1=array([1,2,3,4,5])
ar2=array([6,7,8,9,10])

ar3=ar1 + ar2
print(ar3)

#
arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,10])

print(sin(arr1))
print(cos(arr1))
print(sqrt(arr1))
print(min(arr1))
print(max(arr1))
print(concatenate([arr1,arr2]))

#serious stuff - copy an array
#both the arrays have the same address id
# it is not copy it is directly assign the first array
#in the below example :

arr5=array([2,7,5,3,9])
arr6=arr5
print('arr5 = ',arr5)
print('arr6 = ',arr6)
print('id(arr5) = ',id(arr5))
print('id(arr6) = ',id(arr6))
print()
print()
# this is also called as alising.

arr8=array([2,7,5,3,9])
arr9=arr8.view()
print('arr8 = ',arr8)
print('arr9 = ',arr9)
print('id(arr8) = ',id(arr8))
print('id(arr9) = ',id(arr9))
print()
print()

'''types of copy :
        i. shallow copy
        ii. deep copy
'''
#shallow copy
arr10=array([2,7,5,3,9])
arr11=arr10.view()
arr10[1]=8
print('arr10 = ',arr10)
print('arr11 = ',arr11)
print('id(arr10) = ',id(arr10))
print('id(arr11) = ',id(arr11))
print()
print()

#deep copy
arr12=array([2,7,5,3,9])
arr13=arr12.copy()
arr12[1]=8
print('arr12 = ',arr12)
print('arr13 = ',arr13)
print('id(arr12) = ',id(arr12))
print('id(arr13) = ',id(arr13))
print()
print()

