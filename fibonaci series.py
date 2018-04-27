a=int(input("enter the first number of series"))
b=int(input("enter the first number of series"))
n=int(input("enter the first number of series"))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
