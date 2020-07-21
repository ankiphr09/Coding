# Given an unsorted array of both negative and positive integer. The task is place all negative 
# element at the end of array without changing the order of positive element and negative element.
# Examples:

# Input : arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
# Output : 1  3  2  11  6  -1  -7  -5 

# Input : arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
# Output : 7  9  10  11  -5  -3  -4  -1  

# The problem becomes easier if we are allowed to use extra space. Idea is create an empty array (temp[]). 
# First we store all positive element of given array and 
# then we store all negative element of array in Temp[]. Finally we copy temp[] to original array.

# Python program to Move All -ve Element At End 
# Without changing order Of Array Element 

# Moves all -ve element to end of array in 
# same order. 
def segregateElements(arr, n): 
	# Create an empty array to store result 
	temp = [0 for k in range(n)] 

	# Traversal array and store +ve element in 
	# temp array 
	j = 0 # index of temp 
	for i in range(n): 
		if (arr[i] >= 0 ): 
			temp[j] = arr[i] 
			j +=1

	# If array contains all positive or all negative. 
	if (j == n or j == 0): 
		return

	# Store -ve element in temp array 
	for i in range(n): 
		if (arr[i] < 0): 
			temp[j] = arr[i] 
			j +=1

	# Copy contents of temp[] to arr[] 
	for k in range(n): 
		arr[k] = temp[k] 

# Driver program 
arr = [1 ,-1 ,-3 , -2, 7, 5, 11, 6 ] 
n = len(arr) 

segregateElements(arr, n)

for i in range(n): 
	print(arr[i],end=' ') 

# Time Complexity : O(n)
# Auxiliary space : O(n)