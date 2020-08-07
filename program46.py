#Python|Count the number of matching characters in a pair of strings.
str1=input("Enter first string")
str2=input("Enter second string")
c, j = 0, 0
for i in str1:
	if str2.find(i)>= 0 and j == str1.find(i) :  
		c=c+1
	j+=1
print ('No. of matching characters are : ', c) 