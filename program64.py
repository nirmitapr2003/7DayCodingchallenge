#Python program to find the largest element in an array.
input_string = input("Enter array elements separated by space ")
arr=[]
print("\n")
arr= input_string.split()
n = len(arr) 
max = arr[0] 
for i in range(0, len(arr)):
	if arr[i] > max:    
		max = arr[i]    
print("Largest element present in given array: " + str(max))