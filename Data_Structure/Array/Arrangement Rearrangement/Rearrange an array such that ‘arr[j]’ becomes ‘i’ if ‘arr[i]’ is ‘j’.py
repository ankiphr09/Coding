# # Given an array of size n where all elements are distinct and in range from 0 to n-1, 
# # change contents of arr[] so that arr[i] = j is changed to arr[j] = i.
# # A Simple Solution is to create a temporary array and one by one copy ‘i’ to ‘temp[arr[i]]’ 
# # where i varies from 0 to n-1.

# # A simple Python3 program to rearrange 
# # contents of arr[] such that arr[j] 
# # becomes j if arr[i] is j 

# # A simple method to rearrange 
# # 'arr[0..n-1]' so that 'arr[j]' 
# # becomes 'i' if 'arr[i]' is 'j' 
# def rearrangeNaive(arr, n): 

# 	# Create an auxiliary array 
# 	# of same size 
# 	temp = [0] * n 
	
# 	# Store result in temp[] 
# 	for i in range(0, n): 
# 		temp[arr[i]] = i 

# 	# Copy temp back to arr[] 
# 	for i in range(0, n): 
# 		arr[i] = temp[i] 


# 	# A utility function to print 
# 	# contents of arr[0..n-1] 
# def printArray(arr, n): 
# 	for i in range(0, n): 
# 		print(arr[i], end = " ") 

# # Driver program 
# arr = [1, 3, 0, 2] 
# n = len(arr) 
# print("Given array is", end = " ") 
# printArray(arr, n) 

# rearrangeNaive(arr, n) 
# print("\nModified array is", end = " ") 
# printArray(arr, n) 


# # The time complexity of the above solution is O(n) and auxiliary space needed is O(n).
# A simple Python3 program to rearrange 
# contents of arr[] such that arr[j] 
# becomes j if arr[i] is j 
##################################################################################################

# Another Method: The idea is to store each element’s new and old value as quotient and remainder of n, 
# respectively (n being the size of the array).
# For example, Suppose an element’s new value is 2, the old value is 1 and n is 3, 
# then the element’s value is stored as 1 + 2*3 = 7. We can retrieve its old value by 7%3 = 1 and 
# its new value by 7/3 = 2.

# A simple method to rearrange 
# 'arr[0..n-1]' so that 'arr[j]' 
# becomes 'i' if 'arr[i]' is 'j' 
def rearrange(arr, n): 
	
	for i in range(n): 
		
		# Retrieving old value and 
		# storing with the new one 
		arr[arr[i] % n] += i * n 
	
	for i in range(n): 
		
		# Retrieving new value 
		arr[i] //= n 
	
# A utility function to pr 
# contents of arr[0..n-1] 
def prArray(arr, n): 
	
	for i in range(n): 
		print(arr[i], end = " ") 
	print() 

# Driver code 
arr = [1, 3, 0, 2] 
n = len(arr) 

print("Given array is : ") 
prArray(arr, n) 

rearrange(arr, n) 

print("Modified array is :") 
prArray(arr, n) 
