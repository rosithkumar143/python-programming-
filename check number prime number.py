a=int(raw_input())
if(a<=1000):
  for i in range(2, a):
		if a%i == 0:
			print("no")
			break
  else:
		print("yes")
else:
print("no")
