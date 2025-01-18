from typing import List
# Time complexity O(n)
#space complexity O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer_arr =[1]*n

        for i in range(1,n):
            answer_arr[i] = answer_arr[i-1]* nums[i-1]

        suffix = 1
        for i in range(n-1, -1,-1):
            answer_arr[i] *= suffix
            suffix *=nums[i]
    

        return answer_arr
