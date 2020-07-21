#14.Python Program to Find Factorial of Number 
num = int(input("Enter the number: "))
f= 1
if num < 0:
   print("factorial does not exist for negative numbers")
else:
	i=1
	while i<=num:
   		f=f*i
   		i=i+1
	print("The factorial of",num,"is",f)
	