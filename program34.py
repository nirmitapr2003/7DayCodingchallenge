#Python program to find the sum of all items in a dictionary.
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
sum = 0
for i in myDict: 
    sum = sum +int(myDict[i])
print(sum) 