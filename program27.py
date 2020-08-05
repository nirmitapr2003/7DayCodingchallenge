#Python| Reversing a List.
input_string = input("Enter a list elements separated by space ")
lst=[]
print("\n")
lst = input_string.split()
print("user list is ", lst)
lst.reverse()
print("Using inbuilt function",lst)
input_strin = input("Enter a list elements separated by space ")
lsst=[]
print("\n")
lsst = input_strin.split()
print("user list is ", lsst)
new_lst = lsst[::-1]
print("Using the slicing technique.",new_lst)

