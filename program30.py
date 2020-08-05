#Python program to find the sum of elements in a list.
input_string = input("Enter a list elements separated by space ")
lst=[]
print("\n")
lst = input_string.split()
print("user list is ", lst)
sum=0
for i in range(0,len(lst)):
	sum=sum+int(lst[i])
print("Sum of elements of the list= ",sum)