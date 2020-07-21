#11.Python Program to Sort Words in Alphabetic Order 
input_string = input("Enter a sentence ")
words = input_string.split()
words.sort()
print("The sorted words in the sentence are:")
for word in words:
	print(word)