#6.Write a Python program to remove the first item from a specified list. 
input_string = input("Enter a list elements separated by space ")
userList=[]
print("\n")
userList = input_string.split()
print("user list is ", userList)
del(userList[0])
print(userList)