
#this function example is wasting two lines.
def squ(a):
    return a*a

r=squ(5)
print('r : ',r)


'''
    the below example
    it is saved the lines
    it is a anonymous function
    we can use only one expression in this function
'''
f = lambda a : a*a

res=f(5)
print('res : ',res)

#example2

f1=lambda x,y: x+y

r=f1(5,6)
print('f1 : ',r)

'''
    lambda
    filter
    map
    reduce
'''

'''
    in the list we can fetch only even numbers using filter.
'''
print('using fun & filter :')
def is_even(n):
    return n%2==0

nums=[3,4,5,6,7,8,9,1,55]
print('nums : ',nums)
evens=list(filter(is_even,nums))

print('evens : ',evens)
print()

'''
    in the list we can fetch only even numbers using filter and lambda.
'''
print('using lambda and filter :')
print('nums : ',nums)
evens=list(filter(lambda n : n%2==0,nums))
print('evens : ',evens)
print()

'''
    in the list we can add 2 numbers using map and fun.
'''
def upd(n):
    return n+2

print('using map and fun :')
print('nums : ',nums)
evens=list(filter(lambda n : n%2==0,nums))
doubles = list(map(upd,evens))
print('evens : ',evens)
print()

'''
    in the list we can add 2 numbers using map and lambda.
'''

print('using map and lambda :')
print('nums : ',nums)
add2=list(filter(lambda n : n%2==0,nums))
doubles = list(map(lambda n : n*2,add2))
print('doubles : ',doubles)
print()

'''
    in the list we can add 2 numbers using reduce and fun.
'''
from functools import reduce

print('using reduce and fun : ')
def add_all(a,b):
    return a+b
sum=reduce(add_all,doubles)
print('sum : ',sum)
print()

'''
    in the list we can add 2 numbers using reduce and lambda.
'''

print('using reduce and lambda : ')
sum=reduce(lambda a,b : a+b,doubles)
print('sum : ',sum)
print()

