import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all = sorted(nums1 + nums2)

        middle = math.floor(len(all) / 2)

        first = all[middle]
        if len(all) % 2 == 1:
            return first
        else:
            second = all[middle - 1]
            difference = (first - second)
            middle_of_difference = (difference / 2)
            return middle_of_difference + second
