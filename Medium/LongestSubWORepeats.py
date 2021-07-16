# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    mapper = {}

    longestString = ""
    index = 0
    walker = 0

    while walker != len(s):
        if s[walker] in mapper.keys():
            temp = s[index: walker]

            if len(temp) > len(longestString):
                longestString = temp

            if s[walker] != s[walker - 1] and index <= (walker - 1):
                walker -= 1

            index += 1
            walker = index
            mapper = {}

        else:
            mapper[s[walker]] = 1
            walker += 1

    if longestString == "":
        longestString = s[index: walker]

    elif all([num == 1 for num in mapper.values()]):
        temp = s[index: walker]

        if len(temp) > len(longestString):
            longestString = temp

    return len(longestString)


if __name__ == '__main__':
    assert 3 == lengthOfLongestSubstring("abcabcbb")
    assert 1 == lengthOfLongestSubstring("bbbbb")
    assert 3 == lengthOfLongestSubstring("pwwkew")
    assert 3 == lengthOfLongestSubstring("dvdf")
    assert 5 == lengthOfLongestSubstring("anviaj")
