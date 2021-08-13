# https://leetcode.com/problems/palindrome-number/

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    return str(x) == str(x)[::-1]
