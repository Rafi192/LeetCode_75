#Time complexity -> O(N)
#space complexity -> O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')  # Smallest number
        second = float('inf')  # Second smallest number

        if len(nums)<3:
            return False

        for num in nums:
            if num <= first:
                first = num  # Update the smallest number
            elif num <= second:
                second = num  # Update the second smallest number
            elif num > first and num > second:
                # If we find a number larger than both `first` and `second`
                return True

        return False
