#Python program for bubble sort.
def bubbleSort(ar):
	n = len(ar)
	for i in range(n):
		for j in range(0, n-i-1):
			if ar[j]>ar[j+1] :
				ar[j], ar[j+1] = ar[j+1], ar[j]
input_string = input("Enter a list elements separated by space ")
ar=[]
print("\n")
ar= input_string.split()
bubbleSort(ar)
print ("Sorted array is:")
for i in range(len(ar)):
	print (ar[i])