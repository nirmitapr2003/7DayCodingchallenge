#Different ways to clear a list in python.
input_string = input("Enter a list elements separated by space ")
userList=[]
print("\n")
userList = input_string.split()
print("user list is ", userList)
userList.clear()
print("Clearing list using clear function", userList)
input_strin = input("Enter a list elements separated by space ")
useList=[]
print("\n")
useList = input_strin.split()
print("user list is ", useList)
useList=[]
print("deleting list using reinitialization ", useList)
input_stri = input("Enter a list elements separated by space ")
usList=[]
print("\n")
usList = input_stri.split()
print("user list is ", usList)
usList*=0
print(" deleting list using *= 0 ",usList)
input_str = input("Enter a list elements separated by space ")
uList=[]
print("\n")
uList = input_str.split()
print("user list is ", uList)
del uList[:]
print("deleting list using del ", uList)
