from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap to store value -> index
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is already seen
            if complement in seen:
                return [seen[complement], i]

            # Otherwise, store this number with its index
            seen[num] = i
