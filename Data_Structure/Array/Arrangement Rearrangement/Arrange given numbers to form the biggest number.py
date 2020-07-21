# # Given an array of numbers, arrange them in a way that yields the largest value. 
# # For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 
# # gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, 
# # then the arrangement 998764543431 gives the largest value.
# #----------------------------------------------------------------------------------------------
# # The idea is to use any comparison based sorting algorithm.

# # In the used sorting algorithm, instead of using the default comparison,
# #  write a comparison function myCompare() and use it to sort numbers.

# # Given two numbers X and Y, how should myCompare() decide which number to put first – 
# # we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y). 
# # If XY is larger, then X should come before Y in output, else Y should come before. 
# # For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. 
# # Since 60542 is greater than 54260,
# # we put Y first.
# #------------------------------------------------------------------------------------------------
# # Python3 Program to get the maximum 
# # possible integer from given array 
# # of integers... 


# # custom comparator to sort according 
# # to the ab, ba as mentioned in description 
# def comparator(a, b): 
# 	ab = str(a) + str(b) 
# 	ba = str(b) + str(a) 
# 	return ((int(ba) > int(ab)) - (int(ba) < int(ab))) 
	
# def myCompare(mycmp): 
	
# 	# Convert a cmp= function into a key= function 
# 	class K(object): 
# 		def __init__(self, obj, *args): 
# 			self.obj = obj 
# 		def __lt__(self, other): 
# 			return mycmp(self.obj, other.obj) < 0
# 		def __gt__(self, other): 
# 			return mycmp(self.obj, other.obj) > 0
# 		def __eq__(self, other): 
# 			return mycmp(self.obj, other.obj) == 0
# 		def __le__(self, other): 
# 			return mycmp(self.obj, other.obj) <= 0
# 		def __ge__(self, other): 
# 			return mycmp(self.obj, other.obj) >= 0
# 		def __ne__(self, other): 
# 			return mycmp(self.obj, other.obj) != 0
# 	return K 
# # driver code 
# if __name__ == "__main__": 
# 	a = [54, 546, 548, 60, ] 
# 	sorted_array = sorted(a, key=myCompare(comparator)) 
# 	number = "".join([str(i) for i in sorted_array]) 
# 	print(number) 
#-----------------------------------------------------------------------------------
# Another approach:(using itertools) 
# Using the inbuilt library of the Python, 
# itertools library can be used to perform this task.

# Python3 implementation this is to use itertools. 
# permutations as coded below: 

# Python3 implementation this is to use itertools. 
# permutations as coded below: 

from itertools import permutations 
def largest(l): 
	lst = [] 
	for i in permutations(l, len(l)): 
		# provides all permutations of the list values, 
		# store them in list to find max 
		lst.append("".join(map(str,i))) 
	return max(lst) 

print(largest([54, 546, 548, 60])) #Output 6054854654 

