# An array contains both positive and negative numbers in random order. Rearrange the array elements so that positive and negative numbers 
# are placed alternatively. Number of positive and negative numbers need not be equal. If there are more positive numbers they appear 
# at the end of the array. If there are more negative numbers, they too appear in the end of the array.

# For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9], then the output should be [9, -7, 8, -3, 5, -1, 2, 4, 6]

# Note: The partition process changes relative order of elements. I.e. the order of the appearance of elements is not maintained with 
# this approach. See this for maintaining order of appearance of elements in this problem.

# The solution is to first separate positive and negative numbers using partition process of QuickSort. In the partition process, 
# consider 0 as value of pivot element so that all negative numbers are placed before positive numbers. Once negative and positive numbers 
# are separated, we start from the first negative number and first positive number, and swap every alternate negative number with next 
# positive number.

# Python program to put positive numbers at even indexes (0, // 2, 4,..) and 
# negative numbers at odd indexes (1, 3, 5, ..) 

# The main function that rearranges elements of given array. 
# It puts positive elements at even indexes (0, 2, ..) and 
# negative numbers at odd indexes (1, 3, ..). 
def rearrange(arr, n): 
	# The following few lines are similar to partition process 
	# of QuickSort. The idea is to consider 0 as pivot and 
	# divide the array around it. 
	i = -1
	for j in range(n): 
		if (arr[j] < 0): 
			i += 1
			# swapping of arr 
			arr[i], arr[j] = arr[j], arr[i] 

	# Now all positive numbers are at end and negative numbers 
	# at the beginning of array. Initialize indexes for starting 
	# point of positive and negative numbers to be swapped 
	pos, neg = i+1, 0

	# Increment the negative index by 2 and positive index by 1, 
	# i.e., swap every alternate negative number with next 
	# positive number 
	while (pos < n and neg < pos and arr[neg] < 0): 

		# swapping of arr 
		arr[neg], arr[pos] = arr[pos], arr[neg] 
		pos += 1
		neg += 2

# A utility function to print an array 
def printArray(arr, n): 
	for i in range(n): 
		print(arr[i],end=' ')

# Driver program to test above functions 
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9] 
n = len(arr) 
rearrange(arr, n) 
printArray(arr, n) 

# Time Complexity: O(n) where n is number of elements in given array.
# Auxiliary Space: O(1)