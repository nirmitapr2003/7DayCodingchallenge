#Python program to check if given array is Monotonic.
def isMonotonic(A): 
	return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
			all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
input_string = input("Enter array elements separated by space ")
A=[]
print("\n")
A= input_string.split()
print(isMonotonic(A))
