#Ways to remove the i'th character from string in python.
test_str = input("Enter the word")
n=int(input("Enter the position of the character you want to remove"))
print ("The original string is : " , test_str)
new_str = "" 
if n>len(test_str):
	print("The index position does not exist")
else:
	for i in range(len(test_str)): 
		if i!=n :
			new_str = new_str + test_str[i]
	print ("The string after removal of i'th character : " + new_str) 