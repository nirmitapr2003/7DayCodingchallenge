#Python program to remove the Nth occurrence of the given word.
input_string = input("Enter a list elements separated by space ")
lst=[]
print("\n")
lst = input_string.split()
print("user list is ", lst)
word=input("Enter the word")
N=int(input("Enter the Nth occurance"))
count = 0 
newList=[]
for i in lst: 
    if(i == word): 
        count = count + 1
        if(count != N): 
            newList.append(i) 
    else: 
        newList.append(i) 
              
lst = newList 
      
if count == 0: 
    print("Item not found") 
else: 
    print("Updated list is: ", lst)     