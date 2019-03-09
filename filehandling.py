'''

f=open('text','r')
print(f.read())


f=open('text','r')
print(f.readline(),end="#")
print(f.readline())


f=open('text','r')


f1=open('abc','w')


for data in f:
    f1.write(data)

'''

f=open('1.jpg','rb')
f1=open('2.jpg','wb')

for i in f:
    f1.write(i)

