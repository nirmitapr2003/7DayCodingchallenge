#Remove all duplicates from a given string in Python.
from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
str1=input("Enter a string")     
print(remove_duplicate(str1))