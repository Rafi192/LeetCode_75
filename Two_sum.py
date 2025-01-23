# Two sum problem. Given target sum. find the pair of element that matches with the sum
# solved in polynomial and linear time



#User function Template for python3
# Time -> O(n^2)
# Space -> O(1)

class Solution:
	def twoSum(self, arr, target):
		# code here
		arr_len = len(arr)
		for i in range(arr_len):
		    for j in range(i+1, arr_len):
		        if arr[i] + arr[j] == target:
		            return True
		return False 



# Time complexity -> O(N)
# Space Complexity -> O(1)
class Solution:
	def twoSum(self, arr, target):
		# code here
		arr.sort()
		arr_len = len(arr)
		
		left =0
		right = arr_len-1
		while left < right:
		    match = arr[left] + arr[right]
		    if match== target:
		        return True
		    elif match<target:
		        left +=1
		    elif match > target:
		        right -=1
	    
	    return False
	
