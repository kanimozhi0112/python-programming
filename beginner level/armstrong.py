n=int(input("value"))
s=len(str(n))
temp=n
sum=0
while(n>0):
    dig=n%10
    sum=dig**s+sum
    n=n//10
if(temp==sum):
    print("armstrong")
else:
    print("not armstrong")



