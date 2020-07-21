# 19.Python Program to Find the Factorial of a Number
num=int(input("Enter the number "))
count=0
temp=0
while num>0:
	temp=int(num%10)
	count=count+1
	num=int(num/10)
print("No.of digits=",count)