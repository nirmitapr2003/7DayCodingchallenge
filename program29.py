#Python| Count the occurrences of an element in a list.
input_string = input("Enter a list elements separated by space ")
lst=[]
print("\n")
lst = input_string.split()
print("user list is ", lst)
x=input("Enter the element whose occurrance you want to count")
count = 0
for i in lst: 
    if (i == x): 
        count = count + 1
print(x," has occurred ",count," times in the list")