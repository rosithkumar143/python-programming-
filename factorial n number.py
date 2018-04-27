n=int(input())
if(n==0):
  print("factorial is 1 ")
  
elif(n<0):
  print("positive number alone")
  
elif(n<=20):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  print(fact)
  
else:
  print("invalid")
