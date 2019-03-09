a=int(input('Enter a : '))
b=int(input('Enter b : '))

try:
    print('open1')
    print(a/b)
    k = int(input('Enter k : '))
    print(k)
except ZeroDivisionError as e :
    print(e)
except ValueError as e :
    print(e)
except Exception as e :
    print('Wrong!')
finally:
    print('closed')
print('bye')