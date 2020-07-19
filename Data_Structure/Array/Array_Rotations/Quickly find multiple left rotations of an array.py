# Quickly find multiple left rotations of an array | Set 1
# Efficient Approach:
# The above approaches work well when there is single rotation required. The approaches also modify the original array. To handle multiple queries of array rotation, we use a temp array of size 2n and quickly handle rotations.

# Step 1 : Copy the entire array two times in temp[0..2n-1] array.
# Step 2 : Starting position of array after k rotations in temp[] will be k % n. We do k
# Step 3 : Print temp[] array from k % n to k % n + n.

# Python3 implementation of left rotation 
# of an array K number of times 

# Fills temp with two copies of arr 
# def preprocess(arr, n): 
# 	temp = [None] * (2 * n) 
	
# 	# Store arr elements at i and i + n 
# 	for i in range(n): 
# 		temp[i] = temp[i + n] = arr[i] 
# 	return temp 

# # Function to left rotate an array k times 
# def leftRotate(arr, n, k, temp): 
	
# 	# Starting position of array after k 
# 	# rotations in temp will be k % n 
# 	start = k % n 
	
# 	# Print array after k rotations 
# 	for i in range(start, start + n): 
# 		print(temp[i], end = " ") 
# 	print("") 

# # Driver program 
# arr = [1, 3, 5, 7, 9] 
# n = len(arr) 
# temp = preprocess(arr, n) 

# k = 2
# leftRotate(arr, n, k, temp) 
		
# k = 3
# leftRotate(arr, n, k, temp) 
		
# k = 4
# leftRotate(arr, n, k, temp) 
#------------------------------------------------------------------------------------
# Note that the task to find starting address of rotation takes O(1) time. It is printing the elements that takes O(n) time.

# Space optimized Approach : The above method takes extra space. Below given is the space optimized solution

# Python3 implementation of 
# left rotation of an array 
# K number of times 

# Function to left rotate 
# an array k times 
def leftRotate(arr, n, k): 
	
	# Print array 
	# after k rotations 
	for i in range(k, k + n): 
		print(str(arr[i % n]), 
				end = " ") 

# Driver Code 
arr = [1, 3, 5, 7, 9] 
n = len(arr) 
k = 2 
leftRotate(arr, n, k) 
print() 

k = 3 
leftRotate(arr, n, k) 
print() 

k = 4
leftRotate(arr, n, k) 
print() 

