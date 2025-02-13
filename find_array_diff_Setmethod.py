from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        # Elements in nums1 but not in nums2
        diff1 = list(nums1_set - nums2_set)
        # Elements in nums2 but not in nums1
        diff2 = list(nums2_set - nums1_set)

        return [diff1, diff2]
