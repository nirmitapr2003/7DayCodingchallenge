#Python program for linear search.
def linearsearch(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return -1
input_string = input("Enter a list elements separated by space ")
arr=[]
print("\n")
arr= input_string.split()
x =input("Enter the element you want to search")
print("element found at index "+str(linearsearch(arr,x)))