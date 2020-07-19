# # Method 1: This method discusses the Naive Solution which takes O(n2) amount of time.
# # The solution involves finding the sum of all the elements of the array in each rotation and then deciding the maximum summation value.

# # Approach:A simple solution is to try all possible rotations. Compute sum of i*arr[i] for every rotation and return maximum sum.
# # Algorithm:
# # Rotate the array for all values from 0 to n.
# # Caluclate the sum for each rotations.
# # Check if the maximum sum is greater than the current sum then update the maximum sum.

# # Maximum sum of i*arr[i] among all rotations of a given array
# # A Naive Python 3 program to find 
# # maximum sum rotation 

# import sys 

# # Returns maximum value of i * arr[i] 
# def maxSum(arr, n): 

# 	# Initialize result 
# 	res = -sys.maxsize 

# 	# Consider rotation beginning with i 
# 	# for all possible values of i. 
# 	for i in range(0, n): 


# 		# Initialize sum of current rotation 
# 		curr_sum = 0
	
# 		# Compute sum of all values. We don't 
# 		# acutally rotation the array, but 
# 		# compute sum by finding ndexes when 
# 		# arr[i] is first element 
# 		for j in range(0, n): 
		
# 			index = int((i + j)% n) 
# 			curr_sum += j * arr[index] 
	

# 		# Update result if required 
# 		res = max(res, curr_sum) 
# 	return res 

# # Driver code 
# arr = [8, 3, 1, 2] 
# n = len(arr) 

# print(maxSum(arr, n)) 

# # Complexity Analysis:
# # Time Complexity : O(n2)
# # Auxiliary Space : O(1)
##################################################################################################

# Method 2: This method discusses the efficient solution which solves the problem in O(n) time. In the naive solution, the values were calculated for every rotation. So if that can be done in constant time then the complexity will decrease.

# Approach: The basic approach is to calculate the sum of new rotation from the previous rotations. This brings up a similarity where only the multipliers of first and last element change drastically and the multiplier of every other element increases or decreases by 1. So in this way, the sum of next rotation can be calculated from the sum of present rotation.
# Algorithm:
# The idea is to compute the value of a rotation using values of previous rotation. When an array is rotated by one, following changes happen in sum of i*arr[i].
# Multiplier of arr[i-1] changes from 0 to n-1, i.e., arr[i-1] * (n-1) is added to current value.
# Multipliers of other terms is decremented by 1. i.e., (cum_sum – arr[i-1]) is subtracted from current value where cum_sum is sum of all numbers.
# next_val = curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1);

# next_val = Value of ∑i*arr[i] after one rotation.
# curr_val = Current value of ∑i*arr[i] 
# cum_sum = Sum of all array elements, i.e., ∑arr[i].

# Lets take example {1, 2, 3}. Current value is 1*0+2*1+3*2
# = 8. Shifting it by one will make it {2, 3, 1} and next value
# will be 8 - (6 - 1) + 1*2 = 5 which is same as 2*0 + 3*1 + 1*2

# An efficient Python 3 program to 
# compute maximum sum of i * arr[i] 

def maxSum(arr, n): 

	# Compute sum of all array elements 
	cum_sum = 0
	
	for i in range(0, n): 
		cum_sum += arr[i] 

	# Compute sum of i * arr[i] for 
	# initial configuration. 
	curr_val = 0
	
	for i in range(0, n): 
		curr_val += i * arr[i] 

	# Initialize result 
	res = curr_val 

	# Compute values for other iterations 
	for i in range(1, n): 
	
		# Compute next value using previous 
		# value in O(1) time 
		next_val = (curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1)) 

		# Update current value 
		curr_val = next_val 

		# Update result if required 
		res = max(res, next_val) 
	
	return res 


# Driver code 
arr = [8, 3, 1, 2] 
n = len(arr) 

print(maxSum(arr, n)) 

# Complexity analysis:
# Time Complexity: O(n).
# Since one loop is needed from 0 to n to check all rotations and the sum of the present rotation is calculated from the previous rotations in O(1) time).
# Auxiliary Space: O(1).
# As no extra space is required to so the space complexity will be O(1)
