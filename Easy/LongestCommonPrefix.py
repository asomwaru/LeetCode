# https://leetcode.com/problems/longest-common-prefix/

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    shortItem = len(min(strs, key=len))

    for i in range(shortItem):
        letters = [word[i] for word in strs]

        if shortItem == 1 and len(set(letters)) == 1:
            return strs[0][0]

        if i == 0 and len(set(letters)) != 1:
            return ""

        elif len(set(letters)) != 1:
            return strs[0][0: i]

    return min(strs, key=len)
