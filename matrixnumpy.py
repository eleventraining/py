from numpy import *

arr=array([
            [1,2,3,4,6,8],
            [5,6,7,8,9,10]
          ])

print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

arr1=arr.flatten() # it is flatten the two or three dimensional array into one dimensional array.
print('arr1 = ',arr1)
print()

arr2=arr1.reshape(3,4) #two dimensional array
print('arr2 = ',arr2)
print()

#three dimensional array

arr3=arr1.reshape(2,2,3) #three dimensional array
print('arr3 = \n',arr3)
print()

#Matrices
arr4=array([
                [1,2,3,4],
                [5,6,7,8]
            ])
print('arr4 = \n',arr4)
m=matrix(arr4)
print()
print('m = \n',m)
print()

m1=matrix('1 2 3 4 ; 5 6 7 8')
print('m1 = \n',m1)
print()

m2=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print('m2 = \n',m2)
print()
print('diagonal(m2) = ',diagonal(m2))
print()
print('m2.min() = ',m2.min())
print()
print('m2.max() = ',m2.max())
print()

# addition and multiplication of matrix
m3=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m4=matrix('11 22 3 ; 44 5 16 ; 17 8 19')

m5=m3+m4
print('m5 = \n',m5)
print()

m6=m3*m4
print('m6 = \n',m6)
print()


