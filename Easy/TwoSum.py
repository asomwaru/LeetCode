# https://leetcode.com/problems/two-sum/
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, x in enumerate(nums):
        pair = target - x

        try:
            nextIndex = nums.index(pair, i+1)
        except:
            nextIndex = -1

        if nextIndex != -1:
            return [i, nextIndex]
