#factorial of number
def fact(n):
    f=1
    for i in range(1,n+1):
       f=f*i

    return f

x=5
res=fact(x)
print('res',res)
print()

#factorial usinng recursion
import sys
print('getrecursionlimit() : ',sys.getrecursionlimit())  #we can change limit of recursion
print()

def factorial(v):
    if(n==0):
        return 1

    return n*factorial(n-1)

y=5
result=fact(y)
print('result : ',result)

'''
//this program is infinite loop
i=0

def fur():
    global i
    i+=1
    print('hello py',i)
    fur()

fur()

'''
