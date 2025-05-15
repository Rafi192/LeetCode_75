from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_max = 0
        
        for num in nums:
            if num == 1:
                current_max += 1
            else:
                max_ones = max(max_ones, current_max)
                current_max = 0
        
        # Final check in case the longest sequence is at the end
        max_ones = max(max_ones, current_max)
        
        return max_ones