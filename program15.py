#15.Python Program to Display Fibonacci Sequence . 
#input -  4 , output - 0 1 1 2 
num = int(input("Enter the number: "))
a=0
b=0
c=1
i=0

while i<=num:
	a=b
	b=c
	c=a+b
	print(a,end='')
	if a==num-2:
		break
	i=i+1

	

