#pos=-1
def search(lst,x,n):
    i=0
    for i in range(0,x):
    #while i<len(lst):
        if lst[i]==x:
            #globals()['pos']=i
            return i
        #i=i+1

    return -1;

lst=[2,4,7,9,10]
x=len(lst)
n=8
res=search(lst,n,x)
if res==-1:
    print('Not found ')
else:
    print('found at ',res)
