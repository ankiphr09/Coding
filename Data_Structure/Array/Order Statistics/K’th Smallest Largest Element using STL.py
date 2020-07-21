# # We use set in C++ STL.
# # 1) Insert all elements into a set.
# # 2) Traverse the set and print k-th element.
# // STL based C++ program to find k-th smallest 
# // element. 
# #include <bits/stdc++.h> 
# using namespace std; 

# int kthSmallest(int arr[], int n, int k) 
# { 
# 	// Insert all elements into the set 
# 	set<int> s; 
# 	for (int i = 0; i < n; i++) 
# 		s.insert(arr[i]); 

# 	// Traverse set and print k-th element 
# 	auto it = s.begin(); 
# 	for (int i = 0; i < k - 1; i++) 
# 		it++; 
# 	return *it; 
# } 

# int main() 
# { 
# 	int arr[] = { 12, 3, 5, 7, 3, 19 }; 
# 	int n = sizeof(arr) / sizeof(arr[0]), k = 2; 
# 	cout << "K'th smallest element is "
# 		<< kthSmallest(arr, n, k); 
# 	return 0; 
# } 
# Time complexity of above solution is O(n Log n).