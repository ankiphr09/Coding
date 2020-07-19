# The above problem can be easily solved if O(n) extra space is allowed. 
# It becomes interesting due to the limitations that O(1) extra space and order of appearances.
# The idea is to process array from left to right. 
# While processing, find the first out of place element in the remaining unprocessed array.
# An element is out of place if it is negative and at odd index, or it is positive and at 
# even index. Once we find an out of place element, we find the first element after it with 
# opposite sign. 
# We right rotate the subarray between these two elements (including these two).

# Python3 program to rearrange 
# positive and negative integers 
# in alternate fashion and 
# maintaining the order of positive 
# and negative numbers 

# rotates the array to right by once 
# from index 'outOfPlace to cur' 
def rightRotate(arr, n, outOfPlace, cur): 
	temp = arr[cur] 
	for i in range(cur, outOfPlace, -1): 
		arr[i] = arr[i - 1] 
	arr[outOfPlace] = temp 
	return arr 

def rearrange(arr, n): 
	outOfPlace = -1
	for index in range(n): 
		if(outOfPlace >= 0): 

			# if element at outOfPlace place in 
			# negative and if element at index 
			# is positive we can rotate the 
			# array to right or if element 
			# at outOfPlace place in positive and 
			# if element at index is negative we 
			# can rotate the array to right 
			if((arr[index] >= 0 and arr[outOfPlace] < 0) or
			(arr[index] < 0 and arr[outOfPlace] >= 0)): 
				arr = rightRotate(arr, n, outOfPlace, index) 
				if(index-outOfPlace > 2): 
					outOfPlace += 2
				else: 
					outOfPlace =- 1
					
		if(outOfPlace == -1): 
			
			# conditions for A[index] to 
			# be in out of place 
			if((arr[index] >= 0 and index % 2 == 0) or
			(arr[index] < 0 and index % 2 == 1)): 
				outOfPlace = index 
	return arr 

# Driver Code 
arr = [-5, -2, 5, 2, 4, 
		7, 1, 8, 0, -8] 

print("Given Array is:") 
print(arr) 

print("\nRearranged array is:") 
print(rearrange(arr, len(arr))) 

