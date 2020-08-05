#Python| Cloning or copying a list.
input_string = input("Enter a list elements separated by space ")
lst=[]
print("\n")
lst = input_string.split()
print("user list is ", lst)
li_copy = lst[:]
print("the list after cpoying",li_copy)