#Python| Program to check if a string contains any special character.
import re
def run(string):  
	regex=['[','@_','!','#','$','%','^','&','*','(',')','<','>','?','/','}','{','~',']']
	count=0
	for j in range(0,len(string)):
		for i in range(0,len(regex)):    
			if  string[j]==regex[i] : 
				count=count+1 
	if count>0:
		print("String is accepted")
	else:
		print("String is not accepted")
if __name__ == '__main__' : 
	string = input("Enter a string")  
	run(string) 
#regex=['[','@_','!','#','$','%','^','&','*','(',')','<','>','?','/','\','|',''}','{','~',':',']']