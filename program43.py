#Find the length of the string in python.
sr=input("Enter the string")
print("Length of string using len() function",len(sr))
counter = 0    
for i in sr : 
    counter += 1
print("Length of string using for loop and an operator",counter)
counter1 = 0
while sr[counter1:]: 
    counter1 += 1
print("Length of the string using while loop and slicing",counter1)
