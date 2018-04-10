n=int(input())
temp=n
rev=0
while(n>0):
  x=n%10
  rev=rev*10+x
  n=n/10
if(temp==rev):
  print("palindrome")
else:
print("not palindrome")
