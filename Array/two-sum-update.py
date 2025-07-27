class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #tow sum problem in O(N2) complexity
        '''
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+ nums[j] == target:
                    return [i,j]
        '''
        # two sum problem using O(N) complexity
        n = len(nums)
       # nums.sort() # sorting for two pointer approach
        # using two pointer appraoch to find the sum of two elements in O(N) time

        left = 0
        right = n-1 # assigning left and right pointer for array iteration in O(N) time
'''
        for i in range(n):
            if nums[left] + nums[right] == target:
                return [left,right]

            if target > nums[left] + nums[right]:
                left += 1
                
            else:
                right -= 1
                #the two pointer is a good method but heavily relies on sorting the arary.therefore although this methods find the correct sum, it doesnt mathc with the problems target. 
'''

#Therefore, we need to apply hashmap to find the two sum without affecting the original array.


        
        