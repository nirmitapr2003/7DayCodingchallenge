#12.Python Program to Count the Number of Each Vowel
input_string = input("Enter a word or sentence ")
i=0
count=0
while i<len(input_string):
	val=input_string[i]
	if val=='a':
		count=count+1
	
	elif val=='e':
		count=count+1	
	
	elif val=='i':
		count=count+1
	
	elif val=='o':
		count=count+1
	
	elif val=='u':
		count=count+1
	i=i+1

print("The no.of vowels =" ,count)