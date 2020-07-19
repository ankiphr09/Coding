# Given an array of n elements, create a new array which is a rotation of given array and hamming distance between both the arrays is maximum.
# Hamming distance between two arrays or strings of equal length is the number of positions at which the corresponding character(elements) are different.
# Note: There can be more than one output for the given input.

# Examples:

# Input :  1 4 1
# Output :  2
# Explanation:  
# Maximum hamming distance = 2.
# We get this hamming distance with 4 1 1 
# or 1 1 4 

# input :  N = 4
#          2 4 8 0
# output :  4
# Explanation: 
# Maximum hamming distance = 4
# We get this hamming distance with 4 8 0 2.
# All the places can be occupied by another digit.
# Other solutions can be 8 0 2 4, 4 0 2 8 etc.  

# Create another array which is double the size of the original array, 
# such that the elements of this new array (copy array) are just the elements of the 
# original array repeated twice in the same sequence. Example, 
# if the original array is 1 4 1, then the copy array is 1 4 1 1 4 1.
# Now, iterate through the copy array and find hamming distance with every shift 
# (or rotation). So we check 4 1 1, 1 1 4, 1 4 1, choose the output for which the 
# hamming distance is maximum.

# Python3 code to Find another array 
# such that the hamming distance 
# from the original array is maximum 

# Return the maximum hamming 
# distance of a rotation 
def maxHamming( arr , n ): 

	# arr[] to brr[] two times so 
	# that we can traverse through 
	# all rotations. 
	brr = [0] * (2 * n + 1) 
	for i in range(n): 
		brr[i] = arr[i] 
	for i in range(n): 
		brr[n+i] = arr[i] 
	
	# We know hamming distance 
	# with 0 rotation would be 0. 
	maxHam = 0
	
	# We try other rotations one by 
	# one and compute Hamming 
	# distance of every rotation 
	for i in range(1, n): 
		currHam = 0
		k = 0
		for j in range(i, i + n): 
			if brr[j] != arr[k]: 
				currHam += 1
				k = k + 1
		
		# We can never get more than n. 
		if currHam == n: 
			return n 
		
		maxHam = max(maxHam, currHam) 
	
	return maxHam 

# driver program 
arr = [2, 4, 6, 8] 
n = len(arr) 
print(maxHamming(arr, n)) 


# Time Complexity : O(n*n)