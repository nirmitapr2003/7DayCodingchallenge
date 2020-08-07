#Find words which are greater than given length k.
input_string = input("Enter a string ")
Lst=[]
print("\n")
Lst = input_string.split()
n=int(input("Enter the length of the word"))
for i in range(0,len(Lst)):
	a=len(Lst[i])
	if a==n:
		print(Lst[i])
		