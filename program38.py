#Python|Merging two dictionaries.
def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 
input_string = input("Enter a list elements separated by space for inserting keys in a dictionary: ")
Lst=[]
print("\n")
Lst = input_string.split()
input_string1 = input("Enter a list elements separated by space for inserting corresponding values in a dictionary: ")
Li=[]
print("\n")
Li= input_string1.split()
dict1={}
for i in range(0,len(Lst)):
	dict1[Lst[i]]=Li[i]
print(dict1)
input_string2 = input("Enter a list elements separated by space for inserting keys in a dictionary: ")
lst=[]
print("\n")
lst = input_string2.split()
input_string3 = input("Enter a list elements separated by space for inserting corresponding values in a dictionary: ")
li=[]
print("\n")
li= input_string3.split()
dict2={}
for i in range(0,len(Lst)):
	dict2[lst[i]]=li[i]
print(dict2)
dict3 = Merge(dict1, dict2) 
print(dict3) 