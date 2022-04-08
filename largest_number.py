from functools import cmp_to_key
from typing import List


class Solution:
    def largest_number(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int(" ".join(nums)))


arr = [-1, 3, 5, 7]
cl = Solution()
print(cl.largest_number(arr))
