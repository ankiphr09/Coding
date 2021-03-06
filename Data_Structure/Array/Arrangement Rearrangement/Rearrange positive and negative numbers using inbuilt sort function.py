# There is yet another method to solve this problem. We recursively traverse the array cutting it into two halves (array[start..start] & array[(start + 1)..end], and keep on splitting the array till we reach the last element. Then we start merging it back. The idea is to, at any point, keep the array in proper sequence of negative and positive integers. The merging logic would be:

# (I) If the array[start] is negative, merge the rest of the array as it is, so that the negative numbers’ order is maintained. The reason for this is that since we are tracing back from the recursive calls, we start moving right to left through the array, thus, naturally maintaining the original sequence.

# (II) If the array[start] is positive, merge the rest of the array, but, after right-rotating the half of the array[(start + 1)..end]. The idea for the rotation is to merge the array so that the positive array[start] is always merged with the positive elements. But, the only thing here is that the merged array will have all the positive elements on the left and negative elements on the right. So we reverse the sequence in each recursion to get back the original sequence of negative elements and then positive elements subsequently.

# It can be observed since we reverse the array while merging with a positive first element in each recursion, so the sequence of positive elements, although coming after the negative elements, are in a reverse order. So, as a final step, we reverse only the positive half of the final array, and, subsequently getting the intended sequence.

#------------------------------------------------------------------------------

# Python3 implementation of the above approach 
def printArray(array, length): 
	print("[", end = "") 

	for i in range(length): 
		print(array[i], end = "") 

		if(i < (length - 1)): 
			print(",", end = " ") 
		else: 
			print("]") 

def reverse(array, start, end): 
	while(start < end): 
		temp = array[start] 
		array[start] = array[end] 
		array[end] = temp 
		start += 1
		end -= 1

# Rearrange the array with all negative integers 
# on left and positive integers on right 
# use recursion to split the array with first element 
# as one half and the rest array as another and then 
# merge it with head of the array in each step 
def rearrange(array, start, end): 
	
	# exit condition 
	if(start == end): 
		return

	# rearrange the array except the first 
	# element in each recursive call 
	rearrange(array, (start + 1), end) 

	# If the first element of the array is positive, 
	# then right-rotate the array by one place first 
	# and then reverse the merged array. 
	if(array[start] >= 0): 
		reverse(array, (start + 1), end) 
		reverse(array, start, end) 

# Driver code 
if __name__ == '__main__': 
	array = [-12, -11, -13, -5, -6, 7, 5, 3, 6] 
	length = len(array) 
	countNegative = 0

	for i in range(length): 
		if(array[i] < 0): 
			countNegative += 1

	print("array: ", end = "") 
	printArray(array, length) 
	rearrange(array, 0, (length - 1)) 

	reverse(array, countNegative, (length - 1)) 

	print("rearranged array: ", end = "") 
	printArray(array, length) 
#-------------------------------------------------------------------------------
# Time complexity : O(N)