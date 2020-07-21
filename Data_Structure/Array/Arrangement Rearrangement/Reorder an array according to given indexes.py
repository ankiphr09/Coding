# # Given two integer arrays of same size, “arr[]” and “index[]”, 
# # reorder elements in “arr[]” according to given index array. 
# # It is not allowed to given array arr’s length.

# # Expected time complexity O(n) and auxiliary space O(1)


# # A Simple Solution is to use an auxiliary array temp[] of same size as given arrays. 
# # Traverse the given array and put all elements at their correct place in temp[] using index[]. 
# # Finally copy temp[] to arr[] and set all values of index[i] as i.
# # Python 3 program to sort 
# # an array according to given 
# # indexes 

# # Function to reorder 
# # elements of arr[] according 
# # to index[] 
# def reorder(arr,index, n): 

# 	temp = [0] * n; 

# 	# arr[i] should be 
# 		# present at index[i] index 
# 	for i in range(0,n): 
# 		temp[index[i]] = arr[i] 

# 	# Copy temp[] to arr[] 
# 	for i in range(0,n): 
# 		arr[i] = temp[i] 
# 		index[i] = i 
	
# # Driver program 
# arr = [50, 40, 70, 60, 90] 
# index = [3, 0, 4, 1, 2] 
# n = len(arr) 

# reorder(arr, index, n) 

# print("Reordered array is:") 
# for i in range(0,n): 
# 	print(arr[i],end = " ") 

# print("\nModified Index array is:") 
# for i in range(0,n): 
# 	print(index[i],end = " ") 
#####################################################################################################
# 1) Do following for every element arr[i]
#    a) While index[i] is not equal to i
#        (i)  Store array and index values of the target (or 
#             correct) position where arr[i] should be placed.
#             The correct position for arr[i] is index[i]
#        (ii) Place arr[i] at its correct position. Also
#             update index value of correct position.
#        (iii) Copy old values of correct position (Stored in
#             step (i)) to arr[i] and index[i] as the while 
#             loop continues for i.

# A O(n) time and O(1) extra space Python3 program to 
# sort an array according to given indexes 

# Function to reorder elements of arr[] according 
# to index[] 
def reorder(arr, index, n): 

	# Fix all elements one by one 
	for i in range(0,n): 

		# While index[i] and arr[i] are not fixed 
		while (index[i] != i): 
		
			# Store values of the target (or correct) 
			# position before placing arr[i] there 
			oldTargetI = index[index[i]] 
			oldTargetE = arr[index[i]] 

			# Place arr[i] at its target (or correct) 
			# position. Also copy corrected index for 
			# new position 
			arr[index[i]] = arr[i] 
			index[index[i]] = index[i] 

			# Copy old target values to arr[i] and 
			# index[i] 
			index[i] = oldTargetI 
			arr[i] = oldTargetE 


# Driver program 
arr = [50, 40, 70, 60, 90] 
index= [3, 0, 4, 1, 2] 
n = len(arr) 

reorder(arr, index, n) 

print("Reordered array is:") 
for i in range(0, n): 
	print(arr[i],end=" ") 

print("\nModified Index array is:") 
for i in range(0, n): 
	print(index[i] ,end=" ") 

