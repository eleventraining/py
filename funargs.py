'''In python, pass by value and pass by reference is not working.'''
def upd(x):
    print('x = ',x)
    print('id(x) = ',id(x))
    print()
    x=8
    print('x = ',x)
    print()

def update(lst):
    print('id(lst)x = ',id(lst))

    lst[1]=25
    print('id(lst)x1 = ',id(lst))
    print('x = ',lst)
    print()

a=10
print('id(a) = ',id(a))
print()
upd(a)
print('a = ',a)

lst=[10,20,30]
print('lst = ',lst)
print('id(lst) = ',id(lst))
update(lst)
print('lst = ',lst)