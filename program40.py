#python| Check order of character in string using OrderedDict()
def checkPattern(string, pattern):  
    l = len(pattern) 
    if len(string) < l: 
        return False
    for i in range(l - 1):  
        x = pattern[i] 
        y = pattern[i + 1] 
        last = string.rindex(x)
        first = string.index(y) 
        if last == -1 or first == -1 or last > first: 
            return False
    return True 
if __name__ == "__main__": 
    string = input("Enter the string")
    pattern = input("Enter the pattern")
    print(checkPattern(string, pattern)) 
  

	
  



	