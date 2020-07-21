# The idea is to use an auxiliary array. We maintain two pointers one to leftmost or smallest element 
# and other to rightmost or largest element. We more both pointers toward each other and alternatively 
# copy elements at these pointers to an auxiliary array. Finally, we copy auxiliary array back to 
# the original array.
# Python program to rearrange an array in minimum 
# maximum form 

# Prints max at first position, min at second position 
# second max at third position, second min at fourth 
# position and so on. 
def rearrange(arr, n): 
	# Auxiliary array to hold modified array 
	temp = n*[None] 

	# Indexes of smallest and largest elements 
	# from remaining array. 
	small,large =0,n-1

	# To indicate whether we need to copy rmaining 
	# largest or remaining smallest at next position 
	flag = True

	# Store result in temp[] 
	for i in range(n): 
		if flag is True: 
			temp[i] = arr[large] 
			large -= 1
		else: 
			temp[i] = arr[small] 
			small += 1

		flag = bool(1-flag) 

	# Copy temp[] to arr[] 
	for i in range(n): 
		arr[i] = temp[i] 
	return arr 

# Driver program to test above function 
arr = [1, 2, 3, 4, 5, 6] 
n = len(arr) 
print("Original Array") 
print(arr) 
print("Modified Array") 
print(rearrange(arr, n)) 

# Time Complexity: O(n)
# Auxiliary Space: O(n)

