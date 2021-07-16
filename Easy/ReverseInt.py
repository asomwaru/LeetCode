# https://leetcode.com/problems/reverse-integer/

def reverse(x: int) -> int:
    if x > 0:
        rev = int(str(x)[::-1])

    else:
        x *= -1
        rev = int("-" + str(x)[::-1])

    if rev >= (2**31)-1 or rev <= -(2**31):
        return 0
    else:
        return rev
