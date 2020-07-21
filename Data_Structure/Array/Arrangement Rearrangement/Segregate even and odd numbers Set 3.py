# Given an array of integers, segregate even and odd numbers in the array. All the even numbers should be present first, and then the odd numbers.

# Examples:

# Input : 1 9 5 3 2 6 7 11
# Output : 2 6 5 3 1 9 7 11

# Input : 1 3 2 4 7 6 9 10
# Output : 2 4 6 10 7 1 9 3

# The idea discussed in this post is based on Lomuto’s Partition Scheme

# Maintain a pointer to the position before first odd element in the array.
# Traverse the array and if even number is encountered then swap it with the first odd element.
# Continue the traversal.

# Python3 code to segregate even odd 
# numbers in an array 

# Function to segregate even odd numbers 
def arrayEvenAndOdd(arr,n): 
	i = -1
	j= 0
	while (j!=n): 
		if (arr[j] % 2 ==0): 
			i = i+1

			# Swapping even and odd numbers 
			arr[i],arr[j] = arr[j],arr[i] 
			
		j = j+1
	
	# Printing segregated array 
	for i in arr: 
		print (str(i) + " " ,end='') 
		
# Driver Code 
if __name__=='__main__': 
	arr = [ 1 ,8, 2, 4, 7, 6, 12, 10] 
	n = len(arr) 
	arrayEvenAndOdd(arr,n) 

# Time Complexity : O(n)
# Auxiliary Space : O(1)