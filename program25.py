#Python| Ways to check if an element exists in a list.
input_string = input("Enter a list elements separated by space ")
userList=[]
print("\n")
userList = input_string.split()
print("user list is ", userList)
word=input("Enter th word u want to find in the list ")
count=0
for i in range(0,len(userList)):
	if(userList[i]==word):
		count=count+1
if(count>0):
	print("The word exists in the list")
else:
	print("The word does not exists in the list")

