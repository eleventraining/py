#global keywords
a=10
x=20
print('id(x)',id(x))
print('x : ',x)
def some():
    global a
    a=15
    b=8
    print('some')
    print('a :',a)
    print('b : ',b)
    print()

def something():
    x=9
    print('something')
    z = globals()['x']
    print('id(z)',id(z))
    print('x : ',x)
    print()
    globals()['x']=30
    print('x : ',x)
    print()


some()
something()
print('a : ',a)
print('x : ',x)