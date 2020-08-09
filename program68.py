#Python program for Find reminder of array multiplication divided by n.
def findremainder(arr, lens, n): 
	mul = 1
	for i in range(lens):  
		mul = (mul * (int(arr[i]) % n)) % n 
	  
	return mul % n 
input_string = input("Enter array elements separated by space ")
arr=[]
print("\n")
arr= input_string.split()
lens = len(arr) 
n = int(input("Enter the number u want to divide the product with: "))
print( findremainder(arr, lens, n))