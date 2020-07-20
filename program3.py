#Write a python program to concatenate all elements in a list into a string and return it.
input_string = input("Enter a list elements separated by space ")
userList=[]
print("\n")
userList = input_string.split()
print("user list is ", userList) 
result= ''
for element in userList:
    result += str(element)
print(result)        