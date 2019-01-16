a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))

# a is even or odd
if a%2==0 :
    print("Even")
else:
    print("Odd")

# a,b,c which one is greater number
if a>b:
    print("a > b , c ")
elif b>c:
    print("b > c , a ")
else:
    print("c > a , b")