# Types of function arguments

def sum(x, y):
    c = x + y
    print('c : ', c)
    print()


def person(name, age):
    print('name : ', name)
    print('age : ', age)
    print()


# using keyword or variable name
def sale(og_pr, dis_pr):
    print('original price : ', og_pr)
    print('discount price : ', dis_pr - 55)
    print()


# using default args
def full_name(fname, lname='palkar'):
    print('fname : ', fname)
    print('lname : ', lname)
    print()


# using variable length
def sub(a, *b):
    z = a
    for i in b:
        z = z - i
        print('z : ', z)
    print()


# using variable length
def mul(*p):
    r = 1  # for multiply we can assign r=1 else if we can assign 0 to r the output is zero
    for j in p:
        r = r * j
        print('r : ', r)
    print()


sum(5, 6)
person('nikhil', 19)
sale(dis_pr=900, og_pr=1000)  # using keyword or variable name
full_name('Nikhil')  # use default value
full_name('Nikhil', 'Gaikwad')
sub(155, 6, 34, 32)
mul(2, 6, 8, 9)

