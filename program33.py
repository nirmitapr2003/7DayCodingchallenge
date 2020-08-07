#Python dictionary with keys having multiple inputs.
i=1
x=1
kd={}
while(i>0):
	a=input("Enter key1")
	b=input("Enter key2")
	c=input("Enter the value")
	kd[a,b]=c
	y=int(input("Enter 1 if u want to add elements to the dictionary or enter 0 "))
	x=y
	if(x==1):
		continue
	else:
		break
print(kd)
