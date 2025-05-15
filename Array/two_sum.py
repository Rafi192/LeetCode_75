from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store (number, original index) before sorting
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort()  # Sort based on the number
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            
            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1