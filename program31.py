#Pyhton| Sort dictionaries by key or value.
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
print("Sorting dictionary by key:")
for i in sorted (dictionary) : 
    print ((i, dictionary[i]), end =" ")
print("Sorting dictionary by values")
print(sorted(dictionary.items(), key = 
             lambda kv:(kv[1], kv[0])))

