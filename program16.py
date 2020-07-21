#16.Python program to find the sum of 'n' Fibonacci sequence
num = int(input("Enter the number: "))
a=0
b=0
c=1
i=0
sum=0
while i<=num:
	a=b
	b=c
	c=a+b
	sum=sum+a
	if a==num-2:
		break
	i=i+1
print("Sum of the fibonacci sequence=",sum)