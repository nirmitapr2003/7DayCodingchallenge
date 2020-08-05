#Python program to interchange the first and the last elements in a list.
input_string = input("Enter a list elements separated by space ")
userList=[]
print("\n")
userList = input_string.split()
print("user list is ", userList)
temp=userList[0]
userList[0]=userList[-1]
userList[-1]=temp
print("new user list is ",userList)