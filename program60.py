#Python program for merge sort.
def mergeSort(nlist):
	if len(nlist)>1:
		mid = len(nlist)//2
		lefthalf = nlist[:mid]
		righthalf = nlist[mid:]
 
		mergeSort(lefthalf)
		mergeSort(righthalf)
		i=j=k=0      
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				nlist[k]=lefthalf[i]
				i=i+1
			else:
				nlist[k]=righthalf[j]
				j=j+1
			k=k+1
 
		while i < len(lefthalf):
			nlist[k]=lefthalf[i]
			i=i+1
			k=k+1
 
		while j < len(righthalf):
			nlist[k]=righthalf[j]
			j=j+1
			k=k+1
input_string = input("Enter a list elements separated by space ")
nlist=[]
print("\n")
nlist= input_string.split()  
mergeSort(nlist)
print(nlist)