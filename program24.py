#Python| Ways to find length of a list.
input_string = input("Enter a list elements separated by space ")
userList=[]
print("\n")
userList = input_string.split()
print("user list is ", userList)
print("the length of the list using len() function", len(userList))
print("the lenght of the list without using inbuilt function:")
count=0
for i in userList:
	count=count+1
print(count)