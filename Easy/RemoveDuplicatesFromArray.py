# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    current = 0
    walker = 0

    if len(nums) == 1:
        return len(nums)

    while current < len(nums):
        currentNum = nums[current]

        while walker < len(nums) and nums[walker] == currentNum:
            if walker <= current:
                walker += 1
                continue

            nums.pop(walker)

        current += 1

    return len(nums)
