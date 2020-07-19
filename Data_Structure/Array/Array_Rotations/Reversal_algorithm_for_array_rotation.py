# Method 4 (The Reversal Algorithm) :

# Algorithm :

# rotate(arr[], d, n)
#   reverse(arr[], 1, d) ;
#   reverse(arr[], d + 1, n);
#   reverse(arr[], 1, n);
# Let AB are the two parts of the input array where A = arr[0..d-1] and B = arr[d..n-1]. The idea of the algorithm is :

# Reverse A to get ArB, where Ar is reverse of A.
# Reverse B to get ArBr, where Br is reverse of B.
# Reverse all to get (ArBr) r = BA.
# Example :
# Let the array be arr[] = [1, 2, 3, 4, 5, 6, 7], d =2 and n = 7
# A = [1, 2] and B = [3, 4, 5, 6, 7]

# Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
# Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
# Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]

# Python program for reversal algorithm of array rotation 

# Function to reverse arr[] from index start to end 
def rverseArray(arr, start, end): 
	while (start < end): 
		temp = arr[start] 
		arr[start] = arr[end] 
		arr[end] = temp 
		start += 1
		end = end-1

# Function to left rotate arr[] of size n by d 
def leftRotate(arr, d): 

	if d == 0: 
		return
	n = len(arr) 
	rverseArray(arr, 0, d-1) 
	rverseArray(arr, d, n-1) 
	rverseArray(arr, 0, n-1) 

# Function to print an array 
def printArray(arr): 
	for i in range(0, len(arr)): 
		print(arr[i], end=' ')

# Driver function to test above functions 
arr = [10, 20, 30, 40, 50, 60, 70] 
n = len(arr) 
d = 3

# in case the rotating factor is 
# greater than array length 
d = d % n	 
leftRotate(arr, d) # Rotate array by 2 
printArray(arr) 

# Time Complexity : O(n)