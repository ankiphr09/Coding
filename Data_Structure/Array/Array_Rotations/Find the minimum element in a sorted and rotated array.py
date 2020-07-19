# A simple solution is to traverse the complete array and find minimum. This solution requires O(n) time.
# We can do it in O(Logn) using Binary Search. If we take a closer look at above examples, we can easily figure out following pattern:

# The minimum element is the only element whose previous is greater than it. If there is no previous element element, then there is no rotation (first element is minimum). We check this condition for middle element by comparing it with (mid-1)’th and (mid+1)’th elements.
# If minimum element is not at middle (neither mid nor mid + 1), then minimum element lies in either left half or right half.
# If middle element is smaller than last element, then the minimum element lies in left half
# Else minimum element lies in right half.

# Python program to find minimum element 
# in a sorted and rotated array 

# def findMin(arr, low, high): 
# 	# This condition is needed to handle the case when array is not 
# 	# rotated at all 
# 	if high < low: 
# 		return arr[0] 

# 	# If there is only one element left 
# 	if high == low: 
# 		return arr[low] 

# 	# Find mid 
# 	mid = int((low + high)/2) 

# 	# Check if element (mid+1) is minimum element. Consider 
# 	# the cases like [3, 4, 5, 1, 2] 
# 	if mid < high and arr[mid+1] < arr[mid]: 
# 		return arr[mid+1] 

# 	# Check if mid itself is minimum element 
# 	if mid > low and arr[mid] < arr[mid - 1]: 
# 		return arr[mid] 

# 	# Decide whether we need to go to left half or right half 
# 	if arr[high] > arr[mid]: 
# 		return findMin(arr, low, mid-1) 
# 	return findMin(arr, mid+1, high) 

# # Driver program to test above functions 
# arr1 = [5, 6, 1, 2, 3, 4] 
# n1 = len(arr1) 
# print("The minimum element is " + str(findMin(arr1, 0, n1-1))) 


#################################################################################
# How to handle duplicates?
# Above approach in the worst case(If all the elements are same) take O(N).

# Below is the code to handle duplicates in O(log n) time.

def findMin(arr, low, high): 
    mid =(low + high ) // 2
    if arr[mid]==arr[high]:
        high-=1
    elif arr[mid]>arr[high]:
        low=mid+1
    else: 
        high=mid
    return arr[high]    

# Driver program to test above functions 
arr1 = [5, 6, 1, 2, 3, 4] 
n1 = len(arr1) 
print("The minimum element is " + str(findMin(arr1, 0, n1-1)))
