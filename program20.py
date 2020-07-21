#20.Python Program to Print all Prime Numbers in an Interval
l=int(input("Enter the lower limit: "))
u=int(input("Enter the upper limit: "))
for num in range(l, u+1):
	i=1
	count=0
	while i<=num:
		if num%i==0:
			count=count+1
		i=i+1
	if count==2:
		print(num)
