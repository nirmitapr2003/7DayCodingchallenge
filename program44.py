#Python program to print even length words in a string.
s=input("Enter a string")
s = s.split(' ') 
for word in s: 
	if len(word)%2==0 : 
		print(word) 