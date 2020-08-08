#Python program for insertion sort.
def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j] :
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
input_string = input("Enter a list elements separated by space ")
arr=[]
print("\n")
arr= input_string.split()
insertionSort(arr)
print ("The sorted array is:")
for i in range(len(arr)):
   print (arr[i])