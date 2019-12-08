from collections import defaultdict
from typing import List, Tuple


class Solution:

    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        mapped_nums = defaultdict(lambda: [])
        for i, x in enumerate(nums):
            mapped_nums[x].append(i)
        for num, index in mapped_nums.items():
            left_over = target - num

            if left_over in mapped_nums:
                match = mapped_nums[left_over]
                same_number = match == index and len(match) == 1
                if same_number:
                    continue
                if index[0] in match:
                    return index[0], match[1]
                else:
                    return index[0], match[0]
