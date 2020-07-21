# Given an array, rearrange the array such that :

# If index i is even, arr[i] <= arr[i+1]
# If index i is odd, arr[i] >= arr[i+1]
# Note : There can be multiple answers.

# Examples:

# Input  : arr[] = {2, 3, 4, 5} 
# Output : arr[] = {2, 4, 3, 5}
# Explanation : Elements at even indexes are
# smaller and elements at odd indexes are greater
# than their next elements

# Note : Another valid answer
# is arr[] = {3, 4, 2, 5}

# Input  :arr[] = {6, 4, 2, 1, 8, 3}
# Output :arr[] = {4, 6, 1, 8, 2, 3}

# An efficient solution is to iterate over the array and swap the elements as per the given condition.
# If we have an array of length n, then we iterate from index 0 to n-2 and check the given condition.
# At any point of time if i is even and arr[i] > arr[i+1], then we swap arr[i] and arr[i+1]. Similarly, if i is odd and
# arr[i] < arr[i+1], then we swap arr[i] and arr[i+1].

# For the given example:
# Before rearrange, arr[] = {2, 3, 4, 5}
# Start iterating over the array till index 2 (as n = 4)

# First Step:
# At i = 0, arr[i] = 2 and arr[i+1] = 3. As i is even and arr[i] < arr[i+1], don't need to swap.
# Second step:
# At i = 1, arr[i] = 3 and arr[i+1] = 4. As i is odd and arr[i] < arr[i+1], swap them.
# Now arr[] = {2, 4, 3, 5}
# Third step:
# At i = 2, arr[i] = 3 and arr[i+1] = 5. So, don’t need to swap them

# Python code to rearrange 
# an array such that 
# even index elements 
# are smaller and odd 
# index elements are 
# greater than their 
# next. 

def rearrange(arr, n): 

	for i in range(n - 1): 
		if (i % 2 == 0 and arr[i] > arr[i + 1]): 
		
			temp = arr[i] 
			arr[i]= arr[i + 1] 
			arr[i + 1]= temp 
		
		if (i % 2 != 0 and arr[i] < arr[i + 1]): 
		
			temp = arr[i] 
			arr[i]= arr[i + 1] 
			arr[i + 1]= temp 
			

# Utility that prints out an array in 
# a line 
def printArray(arr, size): 

	for i in range(size): 
		print(arr[i], " ", end ="") 

	print() 

# Driver code 

arr = [ 6, 4, 2, 1, 8, 3 ] 
n = len(arr) 

print("Before rearranging: ") 
printArray(arr, n) 

rearrange(arr, n) 

print("After rearranging:") 
printArray(arr, n)

# Time Complexity :O(n)