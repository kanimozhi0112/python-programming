a=[]
n=int(input("value:"))
for i in range(1,n+1):
    b=int(input("enter the number"))
    a.append(b)
a.sort()
print(a)
b=(a[0])
c=(a[n-1])
print(b,c)
