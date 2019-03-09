#variable length
def per(name,*data):
    print('per')
    print('name : ',name)
    print('data : ',data)
    print()

#kwargs - keyword variable args
def person(nm,**info):
    print('person')
    print('name : ',nm)
    #print('info : ',info)
    for i,j in info.items():
        print(i,j)
    print()

#call functions
per('nikhil',19,'kalyan',9653412755)
person('Nikhil',lnm='Gaikwad',age=19,city='kalyan',clgnm='VESIT')