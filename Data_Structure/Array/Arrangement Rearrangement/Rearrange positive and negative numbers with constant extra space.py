# # A simple solution is to use another array. We copy all elements of original array to new array. We then traverse the new array and copy all negative and positive elements back in original array one by one. This approach is discussed here. The problem with this approach is that it uses auxiliary array and we’re not allowed to use any data structure to solve this problem.

# # One approach that does not use any data structure is to use use partition process of QuickSort. The idea is to consider 0 as pivot and divide the array around it. The problem with this approach is that it changes relative order of elements. 

# # Approach 1: Modified Insertion Sort

# # We can modify insertion sort to solve this problem.

# # Algorithm –

# # Loop from i = 1 to n - 1.
# #   a) If the current element is positive, do nothing.
# #   b) If the current element arr[i] is negative, we 
# #      insert it into sequence arr[0..i-1] such that 
# #      all positive elements in arr[0..i-1] are shifted 
# #      one position to their right and arr[i] is inserted
# #      at index of first positive element.

# # Python 3 program to Rearrange positive 
# # and negative numbers in a array 

# # A utility function to print 
# # an array of size n 
# def printArray(arr, n): 
# 	for i in range(n): 
# 		print(arr[i], end = " ") 
# 	print() 

# # Function to Rearrange positive 
# # and negative numbers in a array 
# def RearrangePosNeg(arr, n): 

# 	for i in range(1, n): 
# 		key = arr[i] 

# 		# if current element is positive 
# 		# do nothing 
# 		if (key > 0): 
# 			continue

# 		''' if current element is negative, 
# 		shift positive elements of arr[0..i-1], 
# 		to one position to their right '''
# 		j = i - 1
# 		while (j >= 0 and arr[j] > 0): 
# 			arr[j + 1] = arr[j] 
# 			j = j - 1

# 		# Put negative element at its 
# 		# right position 
# 		arr[j + 1] = key 

# # Driver Code 
# if __name__ == "__main__": 
# 	arr = [ -12, 11, -13, -5, 
# 			6, -7, 5, -3, -6 ] 
# 	n = len(arr) 

# 	RearrangePosNeg(arr, n) 
# 	printArray(arr, n) 

# # Time complexity of above solution is O(n2) and auxiliary space is O(1). We have maintained the order of appearance and have not used any other data structure.

#------------------------------------------------------------------------------------------

# Approach 2: Optimized Merge Sort
# Merge method of standard merge sort algorithm can be modified to solve this problem. 
# While merging two sorted halves say left and right, we need to merge in such a way that
# negative part of left and right sub-array is copied first followed by positive part of left and 
# right sub-array.

# Python3 program to Rearrange positive 
# and negative numbers in a array 

# Function to pran array 
def printArray(A, size): 

	for i in range(size): 
		print(A[i], end = " ") 
	print() 

# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m + 1..r] 
def merge(arr, l, m, r): 
	i, j, k = 0, 0, 0
	n1 = m - l + 1
	n2 = r - m 

	# create temp arrays */ 
	L = [arr[l + i] for i in range(n1)] 
	R = [arr[m + 1 + j] for j in range(n2)] 

	# Merge the temp arrays back into arr[l..r]*/ 
	i = 0 # Initial index of first subarray 
	j = 0 # Initial index of second subarray 
	k = l # Initial index of merged subarray 

	# Note the order of appearance of elements 
	# should be maintained - we copy elements 
	# of left subarray first followed by that 
	# of right subarray 

	# copy negative elements of left subarray 
	while (i < n1 and L[i] < 0): 
		arr[k] = L[i] 
		k += 1
		i += 1

	# copy negative elements of right subarray 
	while (j < n2 and R[j] < 0): 
		arr[k] = R[j] 
		k += 1
		j += 1

	# copy positive elements of left subarray 
	while (i < n1): 
		arr[k] = L[i] 
		k += 1
		i += 1

	# copy positive elements of right subarray 
	while (j < n2): 
		arr[k] = R[j] 
		k += 1
		j += 1

# Function to Rearrange positive and 
# negative numbers in a array 
def RearrangePosNeg(arr, l, r): 

	if(l < r): 
		
		# Same as (l + r)/2, but avoids 
		# overflow for large l and h 
		m = l + (r - l) // 2

		# Sort first and second halves 
		RearrangePosNeg(arr, l, m) 
		RearrangePosNeg(arr, m + 1, r) 

		merge(arr, l, m, r) 
	
# Driver Code 
arr = [ -12, 11, -13, -5, 
		6, -7, 5, -3, -6 ] 
arr_size = len(arr) 

RearrangePosNeg(arr, 0, arr_size - 1) 

printArray(arr, arr_size) 

