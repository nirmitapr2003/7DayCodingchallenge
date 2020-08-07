#Python| Program to accept the strings which contain all vowels.
string=input("Enter a string")
string = string.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count=0
for i in range(0,len(string)):
	for j in range(0,5):
		if string[i]==vowels[j]:
			count=count+1
if count==len(string):
	print("Accepted")
else:
	print("Not Accepted")

