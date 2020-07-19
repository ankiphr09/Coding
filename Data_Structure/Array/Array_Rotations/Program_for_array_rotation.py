# METHOD 1 (Using temp array)

# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
# 1) Store the first d elements in a temp array
#    temp[] = [1, 2]
# 2) Shift rest of the arr[]
#    arr[] = [3, 4, 5, 6, 7, 6, 7]
# 3) Store back the d elements
#    arr[] = [3, 4, 5, 6, 7, 1, 2]
# Time complexity : O(n)
# Auxiliary Space : O(d)

##############################################################################################

# METHOD 2 (Rotate one by one)

# leftRotate(arr[], d, n)
# start
#   For i = 0 to i < d
#     Left rotate all elements of arr[] by one
# end
# To rotate by one, store arr[0] in a temporary variable temp, move arr[1] to arr[0], arr[2] to arr[1] …and finally temp to arr[n-1]

# Let us take the same example arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2
# Rotate arr[] by one 2 times
# We get [2, 3, 4, 5, 6, 7, 1] after first rotation and [ 3, 4, 5, 6, 7, 1, 2] after second rotation.

##################################################################################################

# Python3 program to rotate an array by 
# d elements 
# Function to left rotate arr[] of size n by d*/ 
# def leftRotate(arr, d, n): 
# 	# for i in range(d):
#     while(d):
#         d=d-1
#         leftRotatebyOne(arr,n)

# # Function to left Rotate arr[] of size n by 1*/ 
# def leftRotatebyOne(arr, n): 
# 	temp = arr[0] 
# 	for i in range(n-1): 
# 		arr[i] = arr[i + 1] 
# 	arr[n-1] = temp 
		

# # utility function to print an array */ 
# def printArray(arr, size): 
# 	for i in range(size): 
# 		print ("% d"% arr[i], end =" ") 


# # Driver program to test above functions */ 
# arr = [10,20,30,40,50,60,70]
# leftRotate(arr, 3, 7) 
# printArray(arr, 7) 

# Time complexity : O(n * d)
# Auxiliary Space : O(1)

###############################################################################################

# METHOD 3 (A Juggling Algorithm)
# This is an extension of method 2. Instead of moving one by one, divide the array in different sets
# where number of sets is equal to GCD of n and d and move the elements within sets.
# If GCD is 1 as is for the above example array (n = 7 and d =2), then elements will be moved within one set only, we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] and finally store temp at the right place.

# Here is an example for n =12 and d = 3. GCD is 3 and

# Python3 program to rotate an array by 
# d elements 
# Function to left rotate arr[] of size n by d 

def leftRotate(arr, d, n): 
	d = d % n 
	g_c_d = gcd(d, n) 
	for i in range(g_c_d): 
		
		# move i-th values of blocks 
		temp = arr[i] 
		j = i 
		while 1: 
			k = j + d 
			if k >= n: 
				k = k - n 
			if k == i: 
				break
			arr[j] = arr[k] 
			j = k 
		arr[j] = temp 

# UTILITY FUNCTIONS 
# function to print an array 
def printArray(arr, size): 
	for i in range(size): 
		print ("% d" % arr[i], end =" ") 

# Fuction to get gcd of a and b 
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b) 

# Driver program to test above functions 
arr = [10, 20, 30, 40, 50, 60, 70] 
n = len(arr) 
d = 2
leftRotate(arr, d, n) 
printArray(arr, n) 

# Time complexity : O(n)
# Auxiliary Space : O(1)