#Handling missing keys in Pyhton dictionaries.
input_string = input("Enter a list elements separated by space for inserting keys in a dictionary: ")
Lst=[]
print("\n")
Lst = input_string.split()
input_string1 = input("Enter a list elements separated by space for inserting corresponding values in a dictionary: ")
Li=[]
print("\n")
Li= input_string1.split()
dictionary={}
for i in range(0,len(Lst)):
	dictionary[Lst[i]]=Li[i]
print(dictionary)
inp=input("Enter the key want to find: ")
print(dictionary.get(inp, 'Not Present'))