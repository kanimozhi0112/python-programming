a=[]
n=int(input("number"))
for i in range(1,n+1):
    b=int(input("enter the number"))
    a.append(b)
    a.sort()
print(a)
print(a[n-1])
