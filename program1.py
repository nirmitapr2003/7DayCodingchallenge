#1.Write a python program to display the first and last colors from the following list.
input_string = input("Enter a list elements separated by space ")
userList=[]
print("\n")
userList = input_string.split()
print("user list is ", userList)
print ("The first element of list is: " + str(userList[0]))
print ("The last element of the list is:" + str(userList[-1])) 


	