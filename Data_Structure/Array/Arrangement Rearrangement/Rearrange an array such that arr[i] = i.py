# Given an array of elements of length N, ranging from 0 to N – 1.
# All elements may not be present in the array. If element is not present then 
# there will be -1 present in the array. Rearrange the array such that A[i] = i 
# and if i is not present, display -1 at that place.

# Approach:
# 1. Nav­i­gate the array.
# 2. Check if a[i] = -1, if yes then ignore it.
# 3. If a[i] != -1, Check if element a[i] is at its cor­rect posi­tion (i=A[i]). 
# If yes then ignore it.
# 4. If a[i] != -1 and ele­ment a[i] is not at its cor­rect posi­tion (i!=A[i]) 
# then place it to its correct posi­tion, 
# but there are two conditions:

# Either A[i] is vacate, means A[i] = -1, then just put A[i] = i .
# OR A[i] is not vacate, means A[i] = x, then int y=x put A[i] = i. 
# Now, we need to place y to its cor­rect place, so repeat from step 3.
# Python3 program for rearrange an 
# array such that arr[i] = i. 

# Function to rearrange an array 
# such that arr[i] = i. 

# def fix( A, len): 
	
# 	for i in range(0, len): 
		
# 		if (A[i] != -1 and A[i] != i): 
# 			x = A[i] 

# 			# check if desired place 
# 			# is not vacate 
# 			while (A[x] != -1 and A[x] != x): 
# 				#store the value from 
# 				# desired place 
# 				y = A[x] 

# 				# place the x to its correct 
# 				# position 
# 				A[x] = x 

# 				# now y will become x, now 
# 				# search the place for x 
# 				x = y 
			
# 			# place the x to its correct 
# 			# position 
# 			A[x] = x

# 			# check if while loop hasn't 
# 			# set the correct value at A[i] 
# 			if (A[i] != i) : 
				
# 				# if not then put -1 at 
# 				# the vacated place 
# 				A[i] = -1

# # Driver function. 
# A = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ] 

# fix(A, len(A)) 

# for i in range(0, len(A)): 
# 	print (A[i],end = ' ') 

######################################################################################

# Python3program for rearrange an 
# array such that arr[i] = i. 


# Function to rearrange an array 
# such that arr[i] = i. 
def fix(A): 
	s = set() 
	
	# Storing all the values in the Set 
	for i in range(len(A)): 
		s.add(A[i]) 

	for i in range(len(A)): 
		# check for item if present in set 
		if i in s: 
			A[i] = i 
		else: 
			A[i] = -1
	return A 
	
# Driver code 
if __name__ == "__main__": 
	A = [-1, -1, 6, 1, 9, 
		3, 2, -1, 4,-1] 
	print(fix(A)) 
