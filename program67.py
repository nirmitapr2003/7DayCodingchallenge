#Python program to split the array and add the first part to the end.
def splitArr(arr, n, k):  
    for i in range(0, k):  
        x = arr[0] 
        for j in range(0, n-1): 
            arr[j] = arr[j + 1]
        arr[n-1] = x

input_string = input("Enter array elements separated by space ")
arr=[]
print("\n")
arr= input_string.split()
n=len(arr)
position=int(input("Enter the position of the element"))
splitArr(arr, n, position) 
  
for i in range(0, n):  
    print(arr[i], end = ' ') 

