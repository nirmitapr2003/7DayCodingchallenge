#10.Python Program to Find all the Factors of a Number
num1 = int(input("Enter the number: "))
f=[]
i=1
while i<=num1:
	if num1%i==0:
		f+=[i]
	i=i+1
print("All factors of the number are: ", f) 
