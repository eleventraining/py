
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[20,30,56,43,79,63,23,13,17,45]

even,odd=count(lst)

print('even : {} \nodd : {}'.format(even,odd))