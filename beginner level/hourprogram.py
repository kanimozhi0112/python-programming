a1=int(input("enter the time1:"))
b1=int(input("enter the minute1:"))
a2=int(input("enter the time2:"))
b2=int(input("enter the minute2:"))
if(a1>0 and a2>0):
    a3=a1-a2
    b3=b1-b2
    print(a3,b3)
else:
    print(-a3,-b3)
    
