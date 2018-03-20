n=int(input("num1"))
q=int(input("num2"))
for a in range(n,q+1):
 if(a>1):
  for i in range(2,a):
    if(a%i==0):
      break
  else:
      print(a)
 
