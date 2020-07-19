# Following are steps.
# 1) Store last element in a variable say x.
# 2) Shift all elements one position ahead.
# 3) Replace first element of array with x.
# Python3 code for program to 
# cyclically rotate an array by one 

# Method for rotation 
def rotate(arr, n): 
	x = arr[n - 1] 
	
	for i in range(n - 1, 0, -1): 
		arr[i] = arr[i - 1] 
		
	arr[0] = x 


# Driver function 
arr= [10, 20, 30, 40, 50] 
n = len(arr) 
print ("Given array is") 
for i in range(0, n): 
	print (arr[i], end = ' ') 

rotate(arr, n) 

print ("\nRotated array is") 
for i in range(0, n): 
	print (arr[i], end = ' ') 

# Time Complexity: O(n) As we need to iterate through all the elements
# Auxiliary Space: O(1)