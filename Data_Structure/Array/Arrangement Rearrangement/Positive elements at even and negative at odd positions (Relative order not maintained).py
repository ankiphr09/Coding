# You have been given an array and you have to make a program to convert that array such that positive elements occur at even numbered places in the array and negative elements occur at odd numbered places in the array. We have to do it in place.

# There can be unequal number of positive and negative values and the extra values have to left as it is.
# Examples:

# Input : arr[] = {1, -3, 5, 6, -3, 6, 7, -4, 9, 10}
# Output : arr[] = {1, -3, 5, -3, 6, 6, 7, -4, 9, 10}

# Input : arr[] = {-1, 3, -5, 6, 3, 6, -7, -4, -9, 10}
# Output : arr[] = {3, -1, 6, -5, 3, -7, 6, -4, 10, -9}
# We take two pointers positive and negative. We set the positive pointer at start of the array and the negative pointer at 1st position of the array.
# We move positive pointer two steps forward till it finds a negative element. Similarly we move negative pointer forward by two places till it finds a positive value at its position.
# If the positive and negative pointers are in the array then we will swap the values at these indexes otherwise we will stop executing the process.

# Python 3 program to rearrange 
# positive and negative numbers 

def rearrange(a, size) : 
	
	positive = 0
	negative = 1

	while (True) : 
		
		# Move forward the positive 
		# pointer till negative number 
		# number not encountered 
		while (positive < size and a[positive] >= 0) : 
			positive = positive + 2

		# Move forward the negative 
		# pointer till positive number 
		# number not encountered 
		while (negative < size and a[negative] <= 0) : 
			negative = negative + 2

		# Swap array elements to fix 
		# their position. 
		if (positive < size and negative < size) : 
			temp = a[positive] 
			a[positive] = a[negative] 
			a[negative] = temp 

		# Break from the while loop when 
		# any index exceeds the size of 
		# the array 
		else : 
			break
		
# Driver code 
arr =[ 1, -3, 5, 6, -3, 6, 7, -4, 9, 10 ] 
n = len(arr) 

rearrange(arr, n) 
for i in range(0, n) : 
	print(arr[i], end = " ") 
