#Python|Check if a substring is present in the string.
string=input("Enter the string ")
sub_str=input("Enter the sub string ")
if (string.find(sub_str) == -1): 
    print("NO") 
else: 
    print("YES") 