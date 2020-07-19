# Python3 code for above implementation 

def leftRotate(arr, d, n): 
	if(d == 0 or d == n): 
		return
	i = d 
	j = n - d 
	while (i != j): 
		
		if(i < j): # A is shorter 
			swap(arr, d - i, d + j - i, i) 
			j -= i 
		
		else: # B is shorter 
			swap(arr, d - i, d, j) 
			i -= j 
	
	swap(arr, d - i, d, i) 

def swap(arr, fi, si, d):
    for i in range(d):
        temp=arr[fi+i]
        arr[fi+i]=arr[si+i]
        arr[si+i]=temp
    
# UTILITY FUNCTIONS 
# function to print an array 
def printArray(arr, size): 
	for i in range(size): 
		print ("% d" % arr[i], end =" ") 


# Driver program to test above functions 
arr = [10, 20, 30, 40, 50, 60, 70] 
n = len(arr) 
d = 10
d = d % n
leftRotate(arr, d, n) 
printArray(arr, n)