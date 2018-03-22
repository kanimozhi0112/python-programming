n1=int(input("number1"))
n2=int(input("number2"))
for i in range(n1,n2+1):
    s=len(str(i))
    temp=i
    sum=0
    while(temp>0):
         dig=temp%10
         sum=dig**s+sum
         temp=temp//10
    if(i==sum):
          print(i)
