
# creating a function
def greet():
    print('Hello')
    print('Good Morning, Python ',end='')

def add(x,y):
    c=x+y
    print(c)

def add1(a,b):
    z=a+b
    return z

def add_sub(p,q):
    r=p+q
    s=p-q
    return r,s

#call function
greet()     #default/without parameteres
add(5,6)    #with parameters
res=add1(5,8)
print('res = ',res)
res1=add_sub(20,15)
print('\nres1 = ',res1)
