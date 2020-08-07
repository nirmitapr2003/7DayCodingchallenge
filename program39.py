#Create grade calculator in python.
name=input("Enter the name of the student")
input_string = input("Enter a list elements separated by space for inserting keys in a dictionary: ")
ass=[]
print("\n")
ass = input_string.split()
input_string1 = input("Enter a list elements separated by space for inserting keys in a dictionary: ")
test=[]
print("\n")
test = input_string1.split()
input_string2 = input("Enter a list elements separated by space for inserting keys in a dictionary: ")
lab=[]
print("\n")
lab= input_string2.split()
a=0
b=0
c=0
i=0
while i<len(ass):
	a=a+int(ass[i])
	i=i+1
j=0
while j<len(test):
	b=b+int(test[j])
	j=j+1
k=0
while k<len(lab):
	c=c+int(lab[k])
	k=k+1
s=a+b+c
per=(a/500)*100
print("name:",name)
print("percentage:",per)
if per >= 90: 
	print("A grade")
elif per >= 80: 
	print("B grade")
elif per >= 70: 
	print("C grade")
elif per >= 60: 
	print("D grade")
else : 
	print("E grade")

	

