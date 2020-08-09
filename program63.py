#Python program to find sum array.
input_string = input("Enter array elements separated by space ")
userList=[]
print("\n")
userList = input_string.split()
print("array=", userList)
sum=0
for i in range(0,len(userList)):
	sum=sum+int(userList[i])
print(sum)