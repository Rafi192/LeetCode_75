#Time complexity - O(N)
#Space Complexity - O(1)


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
    
        num_of_op = 0
        n = len(nums)

        if n== 0:
            return num_of_op
        left = 0
        right = n-1
        while left< right:
            if nums[left]+nums[right] == k:
                num_of_op +=1 
            left +=1
            right -=1
        return num_of_op

