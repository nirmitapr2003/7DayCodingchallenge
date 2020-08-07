#Ways to sort list of dictionaries by values in Python- Using lambda function.
input_string1 = input("Enter a list elements separated by space for inserting corresponding names in a dictionary: ")
Li=[]
print("\n")
Li= input_string1.split()
input_string = input("Enter a list elements separated by space for inserting corresponding age in a dictionary: ")
Lst=[]
print("\n")
Lst= input_string.split()
kd=[]
myDict={}
for i in range(0,len(Lst)):
	myDict={"name":Li[i], "age":Lst[i]}
	kd.append(myDict)
print(kd)

print ("The list printed sorting by age: ")
print (sorted(kd, key = lambda i: i['age']))