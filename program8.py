#8.Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
sum=num1+num2+num3
product=1
if num1==num2 and num2==num3:
	product=sum*3
	print(product)
else: print(sum)

