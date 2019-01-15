a=5
b=6

print(a)
print(b)

#without using third variable
a=a+b #11
b=a-b #5
a=a-b #6

print(a)
print(b)

#using third variable
tmp=a
a=b
b=tmp

print(a)
print(b)

#xor
a=a^b 
b=a^b 
a=a^b 

print(a)
print(b)

#py inbuilt
a,b=b,a #reverse

print(a)
print(b)
