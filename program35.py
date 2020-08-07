#Python| Ways to remove a key from dicitonary.
input_string = input("Enter a list elements separated by space for inserting keys in a dictionary: ")
Lst=[]
print("\n")
Lst = input_string.split()
input_string1 = input("Enter a list elements separated by space for inserting corresponding values in a dictionary: ")
Li=[]
print("\n")
Li= input_string1.split()
myDict={}
for i in range(0,len(Lst)):
	myDict[Lst[i]]=Li[i]
print(myDict)
a=input("Enter the key u want to delete")
print("Deleting key using del function")
del myDict[a]
b=input("Enter the key u want to delete")
print("Deleting key using pop function")
removed_value = myDict.pop(b)
print("After deleting the keys in the dictionary: ",myDict)