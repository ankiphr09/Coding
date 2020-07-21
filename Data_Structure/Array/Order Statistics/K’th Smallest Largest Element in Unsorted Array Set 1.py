# Method 1 (Simple Solution)
# A simple solution is to sort the given array using a O(N log N) sorting algorithm like Merge Sort, Heap Sort, etc and return the element at index k-1 in the sorted array.

# Time Complexity of this solution is O(N Log N)

# Python3 program to find k'th smallest 
# element 

# Function to return k'th smallest 
# element in a given array 
# def kthSmallest(arr, n, k): 

# 	# Sort the given array 
# 	arr.sort() 

# 	# Return k'th element in the 
# 	# sorted array 
# 	return arr[k-1] 

# # Driver code 
# if __name__=='__main__': 
# 	arr = [12, 3, 5, 7, 19] 
# 	n = len(arr) 
# 	k = 2
# 	print(k,"st/nd/rd/th"," smallest element is", 
# 		kthSmallest(arr, n, k)) 
#---------------------------------------------------------------------------------------------------------
# Method 2 (Using Min Heap – HeapSelect)
# We can find k’th smallest element in time complexity better than O(N Log N). 
# A simple optomization is to create a Min Heap of the given n elements and call extractMin() k times.

# // A C++ program to find k'th smallest element using min heap 
# #include <climits> 
# #include <iostream> 
# using namespace std; 

# // Prototype of a utility function to swap two integers 
# void swap(int* x, int* y); 

# // A class for Min Heap 
# class MinHeap { 
# 	int* harr; // pointer to array of elements in heap 
# 	int capacity; // maximum possible size of min heap 
# 	int heap_size; // Current number of elements in min heap 
# public: 
# 	MinHeap(int a[], int size); // Constructor 
# 	void MinHeapify(int i); // To minheapify subtree rooted with index i 
# 	int parent(int i) { return (i - 1) / 2; } 
# 	int left(int i) { return (2 * i + 1); } 
# 	int right(int i) { return (2 * i + 2); } 

# 	int extractMin(); // extracts root (minimum) element 
# 	int getMin() { return harr[0]; } // Returns minimum 
# }; 

# MinHeap::MinHeap(int a[], int size) 
# { 
# 	heap_size = size; 
# 	harr = a; // store address of array 
# 	int i = (heap_size - 1) / 2; 
# 	while (i >= 0) { 
# 		MinHeapify(i); 
# 		i--; 
# 	} 
# } 

# // Method to remove minimum element (or root) from min heap 
# int MinHeap::extractMin() 
# { 
# 	if (heap_size == 0) 
# 		return INT_MAX; 

# 	// Store the minimum vakue. 
# 	int root = harr[0]; 

# 	// If there are more than 1 items, move the last item to root 
# 	// and call heapify. 
# 	if (heap_size > 1) { 
# 		harr[0] = harr[heap_size - 1]; 
# 		MinHeapify(0); 
# 	} 
# 	heap_size--; 

# 	return root; 
# } 

# // A recursive method to heapify a subtree with root at given index 
# // This method assumes that the subtrees are already heapified 
# void MinHeap::MinHeapify(int i) 
# { 
# 	int l = left(i); 
# 	int r = right(i); 
# 	int smallest = i; 
# 	if (l < heap_size && harr[l] < harr[i]) 
# 		smallest = l; 
# 	if (r < heap_size && harr[r] < harr[smallest]) 
# 		smallest = r; 
# 	if (smallest != i) { 
# 		swap(&harr[i], &harr[smallest]); 
# 		MinHeapify(smallest); 
# 	} 
# } 

# // A utility function to swap two elements 
# void swap(int* x, int* y) 
# { 
# 	int temp = *x; 
# 	*x = *y; 
# 	*y = temp; 
# } 

# // Function to return k'th smallest element in a given array 
# int kthSmallest(int arr[], int n, int k) 
# { 
# 	// Build a heap of n elements: O(n) time 
# 	MinHeap mh(arr, n); 

# 	// Do extract min (k-1) times 
# 	for (int i = 0; i < k - 1; i++) 
# 		mh.extractMin(); 

# 	// Return root 
# 	return mh.getMin(); 
# } 

# // Driver program to test above methods 
# int main() 
# { 
# 	int arr[] = { 12, 3, 5, 7, 19 }; 
# 	int n = sizeof(arr) / sizeof(arr[0]), k = 2; 
# 	cout << "K'th smallest element is " << kthSmallest(arr, n, k); 
# 	return 0; 
# } 
#------------------------------------------------------------------------------------
# Method 3 (Using Max-Heap)
# We can also use Max Heap for finding the k’th smallest element. Following is algorithm.
# 1) Build a Max-Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)
# 2) For each element, after the k’th element (arr[k] to arr[n-1]), compare it with root of MH.
# ……a) If the element is less than the root then make it root and call heapify for MH
# ……b) Else ignore it.
# // The step 2 is O((n-k)*logk)

# 3) Finally, root of the MH is the kth smallest element.

# Time complexity of this solution is O(k + (n-k)*Logk)

# // A C++ program to find k'th smallest element using max heap 
# #include <climits> 
# #include <iostream> 
# using namespace std; 

# // Prototype of a utility function to swap two integers 
# void swap(int* x, int* y); 

# // A class for Max Heap 
# class MaxHeap { 
# 	int* harr; // pointer to array of elements in heap 
# 	int capacity; // maximum possible size of max heap 
# 	int heap_size; // Current number of elements in max heap 
# public: 
# 	MaxHeap(int a[], int size); // Constructor 
# 	void maxHeapify(int i); // To maxHeapify subtree rooted with index i 
# 	int parent(int i) { return (i - 1) / 2; } 
# 	int left(int i) { return (2 * i + 1); } 
# 	int right(int i) { return (2 * i + 2); } 

# 	int extractMax(); // extracts root (maximum) element 
# 	int getMax() { return harr[0]; } // Returns maximum 

# 	// to replace root with new node x and heapify() new root 
# 	void replaceMax(int x) 
# 	{ 
# 		harr[0] = x; 
# 		maxHeapify(0); 
# 	} 
# }; 

# MaxHeap::MaxHeap(int a[], int size) 
# { 
# 	heap_size = size; 
# 	harr = a; // store address of array 
# 	int i = (heap_size - 1) / 2; 
# 	while (i >= 0) { 
# 		maxHeapify(i); 
# 		i--; 
# 	} 
# } 

# // Method to remove maximum element (or root) from max heap 
# int MaxHeap::extractMax() 
# { 
# 	if (heap_size == 0) 
# 		return INT_MAX; 

# 	// Store the maximum vakue. 
# 	int root = harr[0]; 

# 	// If there are more than 1 items, move the last item to root 
# 	// and call heapify. 
# 	if (heap_size > 1) { 
# 		harr[0] = harr[heap_size - 1]; 
# 		maxHeapify(0); 
# 	} 
# 	heap_size--; 

# 	return root; 
# } 

# // A recursive method to heapify a subtree with root at given index 
# // This method assumes that the subtrees are already heapified 
# void MaxHeap::maxHeapify(int i) 
# { 
# 	int l = left(i); 
# 	int r = right(i); 
# 	int largest = i; 
# 	if (l < heap_size && harr[l] > harr[i]) 
# 		largest = l; 
# 	if (r < heap_size && harr[r] > harr[largest]) 
# 		largest = r; 
# 	if (largest != i) { 
# 		swap(&harr[i], &harr[largest]); 
# 		maxHeapify(largest); 
# 	} 
# } 

# // A utility function to swap two elements 
# void swap(int* x, int* y) 
# { 
# 	int temp = *x; 
# 	*x = *y; 
# 	*y = temp; 
# } 

# // Function to return k'th largest element in a given array 
# int kthSmallest(int arr[], int n, int k) 
# { 
# 	// Build a heap of first k elements: O(k) time 
# 	MaxHeap mh(arr, k); 

# 	// Process remaining n-k elements. If current element is 
# 	// smaller than root, replace root with current element 
# 	for (int i = k; i < n; i++) 
# 		if (arr[i] < mh.getMax()) 
# 			mh.replaceMax(arr[i]); 

# 	// Return root 
# 	return mh.getMax(); 
# } 

# // Driver program to test above methods 
# int main() 
# { 
# 	int arr[] = { 12, 3, 5, 7, 19 }; 
# 	int n = sizeof(arr) / sizeof(arr[0]), k = 4; 
# 	cout << "K'th smallest element is " << kthSmallest(arr, n, k); 
# 	return 0; 
# }

#---------------------------------------------------------------------------------------------
# Method 4 (QuickSelect)
# This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first step. 
# In QuickSort, we pick a pivot element, then move the pivot element to its correct position and 
# partition the array around it. The idea is, not to do complete quicksort, but stop at the point
#  where pivot itself is k’th smallest element. Also, not to recur for both left and right sides of pivot, 
#  but recur for one of them according to the position of pivot. 
# The worst case time complexity of this method is O(n2), but it works in O(n) on average.

# This function returns k'th smallest element 
# in arr[l..r] using QuickSort based method. 
# ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT 
import sys 

def kthSmallest(arr, l, r, k): 

	# If k is smaller than number of 
	# elements in array 
	if (k > 0 and k <= r - l + 1): 
	
		# Partition the array around last 
		# element and get position of pivot 
		# element in sorted array 
		pos = partition(arr, l, r) 

		# If position is same as k 
		if (pos - l == k - 1): 
			return arr[pos] 
		if (pos - l > k - 1): # If position is more, 
							# recur for left subarray 
			return kthSmallest(arr, l, pos - 1, k) 

		# Else recur for right subarray 
		return kthSmallest(arr, pos + 1, r, 
							k - pos + l - 1) 

	# If k is more than number of 
	# elements in array 
	return sys.maxsize 

# Standard partition process of QuickSort(). 
# It considers the last element as pivot and 
# moves all smaller element to left of it 
# and greater elements to right 
def partition(arr, l, r): 

	x = arr[r] 
	i = l 
	for j in range(l, r): 
		if (arr[j] <= x): 
			arr[i], arr[j] = arr[j], arr[i] 
			i += 1
	arr[i], arr[r] = arr[r], arr[i] 
	return i 

# Driver Code 
if __name__ == "__main__": 
	
	arr = [12, 3, 5, 7, 4, 19, 26] 
	n = len(arr) 
	k = 3 
	print("K'th smallest element is", 
		kthSmallest(arr, 0, n - 1, k)) 
