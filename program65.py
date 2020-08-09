#Python program for array rotation.
def leftRotate(arr, d, n): 
	for i in range(d): 
		leftRotatebyOne(arr, n) 
def leftRotatebyOne(arr, n): 
	temp = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i+1] 
	arr[n-1] = temp 
def printArray(arr,size): 
	for i in range(size): 
		print ("%d"% int(arr[i]),end=" ")
input_string = input("Enter array elements separated by space ")
arr=[]
print("\n")
arr= input_string.split() 
n = len(arr) 
a=int(input("Enter the no.of elements you want to rotate."))
leftRotate(arr, a, n) 
printArray(arr, n) 