d=[]
k=int(input("value"))
for i in range(1,k+1):
 c=int(input("numbers"))
 d.append(c)
 d.sort()
print(d)
print(d[k//2])
