#Python program to count number of vowels using sets in given string.
stri=input("Enter the string")
count = 0
vowel = set("aeiouAEIOU")
for alphabet in stri:
	if alphabet in vowel: 
		count=count+1
print("No. of vowels :", count)