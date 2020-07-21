# # Given a sorted array of positive integers, rearrange the array alternately i.e first element 
# # should be the maximum value, second minimum value, third-second max, fourth-second min and so on


# # # In this post a solution that requires O(n) time and O(1) extra space is discussed. The idea is to 
# # # use multiplication and modular trick to store two elements at an index.
# # even index : remaining maximum element.
# # odd index  : remaining minimum element.
 
# # max_index : Index of remaining maximum element
# #             (Moves from right to left)
# # min_index : Index of remaining minimum element
# #             (Moves from left to right)

# # Initialize: max_index = 'n-1'
# #             min_index = 0  
# #             max_element = arr[max_index] + 1 //can be any element which is more than the maximum value in array

# # For i = 0 to n-1            
# #     If 'i' is even
# #        arr[i] += arr[max_index] % max_element * max_element 
# #        max_index--     
# #     ELSE // if 'i' is odd
# #        arr[i] +=  arr[min_index] % max_element * max_element
# #        min_index++

# # How does expression “arr[i] += arr[max_index] % max_element * max_element” work ?
# # The purpose of this expression is to store two elements at index arr[i]. 
# # arr[max_index] is stored as multiplier and “arr[i]” is stored as remainder. 
# # For example in {1 2 3 4 5 6 7 8 9}, max_element is 10 and we store 91 at index 0. 
# # With 91, we can get original element as 91%10 and new element as 91/10.

# # Python3 program to rearrange an 
# # array in minimum maximum form 

# # Prints max at first position, min at second position 
# # second max at third position, second min at fourth 
# # position and so on. 
# def rearrange(arr, n): 

# 	# Initialize index of first minimum 
# 	# and first maximum element 
# 	max_idx = n - 1
# 	min_idx = 0

# 	# Store maximum element of array 
# 	max_elem = arr[n-1] + 1

# 	# Traverse array elements 
# 	for i in range(0, n) : 

# 		# At even index : we have to put maximum element 
# 		if i % 2 == 0 : 
# 			arr[i] += (arr[max_idx] % max_elem ) * max_elem 
# 			max_idx -= 1

# 		# At odd index : we have to put minimum element 
# 		else : 
# 			arr[i] += (arr[min_idx] % max_elem ) * max_elem 
# 			min_idx += 1

# 	# array elements back to it's original form 
# 	for i in range(0, n) : 
# 		arr[i] = arr[i] / max_elem 


# # Driver Code 
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# n = len(arr) 

# print ("Original Array") 

# for i in range(0, n): 
# 	print (arr[i], end = " ") 
	
# rearrange(arr, n) 

# print ("\nModified Array") 
# for i in range(0, n): 
# 	print (int(arr[i]), end = " ") 
# #---------------------------------------------------------------------------------------------------
# Another Approach: A simpler approach will be to observe indexing positioning of maximum elements and minimum elements. The even index stores maximum elements and the odd index stores the minimum elements. With every increasing index, the maximum element decreases by one and the minimum element increases by one. A simple traversal can be done and arr[] can be filled in again.

# Note: This approach is only valid when elements of given sorted array are consecutive i.e., vary by one unit.

# Python 3 program to rearrange an 
# array in minimum maximum form 

# Prints max at first position, min 
# at second position second max at 
# third position, second min at 
# fourth position and so on. 
def rearrange(arr, n): 

	# initialize index of first minimum 
	# and first maximum element 
	max_ele = arr[n - 1] 
	min_ele = arr[0] 

	# traverse array elements 
	for i in range(n): 
		
		# at even index : we have to 
		# put maximum element 
		if i % 2 == 0: 
			arr[i] = max_ele 
			max_ele -= 1

		# at odd index : we have to 
		# put minimum element 
		else: 
			arr[i] = min_ele 
			min_ele += 1

# Driver code 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
n = len(arr) 
print("Origianl Array") 
for i in range(n): 
	print(arr[i], end = " ") 

rearrange(arr, n) 
print("\nModified Array") 
for i in range(n): 
	print(arr[i], end = " ") 
