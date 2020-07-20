# 7.Write a Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days
from datetime import date
input_string = input("Enter date 1 in the order- year month day ")
input1_string = input("Enter date 2 in the order- year month day ")

num1 = int(input_string[0:4])
num2 = int(input_string[5:7])
num3 = int(input_string[8:10])
n1 = int(input1_string[0:4])
n2 = int(input1_string[5:7])
n3 = int(input1_string[8:10])
print(num1,num2,num3)
print(n1,n2,n3)
f_date = date(num1, num2, num3)
l_date = date(n1, n2, n3)
delta = l_date - f_date
print(delta.days)