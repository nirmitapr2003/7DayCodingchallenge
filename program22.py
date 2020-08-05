#Python program to swap two elements in a list. 
input_string = input("Enter a list elements separated by space ")
userList=[]
n=int(input("Enter the index position of the first element you want to swap"))
m=int(input("Enter the index position of the second element you want to swap"))
print("\n")
userList = input_string.split()
print("user list is ", userList)
x=len(userList)
if(n>x and m>x):
	print("The index position does not exist")
else:
	temp=userList[n]
	userList[n]=userList[m]
	userList[m]=temp
	print("new user list is ",userList)