a=int(raw_input())
b=int(raw_input())
if(b<=1000 and a<=1000):
  for i in range(a,b+1):
    if(i%2==0):
      print(i)
else:
  print("invalid")
    
