#Reconstruct the array by replacing arr[i]with(arr[i-1]+1)%M.
def construct(n, m, a): 
    ind = 0
    for i in range(n): 
        if (int(a[i])!=-1): 
            ind = i 
            break
    for i in range(ind-1, -1, -1): 
        if (int(a[i])==-1): 
            a[i]=(int(a[i + 1])-1 + m)% m  
    for i in range(ind + 1, n): 
        if(int(a[i])==-1): 
            a[i]=(int(a[i-1])+1)% m 
    print(*a)  
n =int(input("Enter value of n"))
m=int(input("Enter value of m"))
input_string = input("Enter array elements separated by space ")
a=[]
print("\n")
a= input_string.split()
construct(n, m, a) 