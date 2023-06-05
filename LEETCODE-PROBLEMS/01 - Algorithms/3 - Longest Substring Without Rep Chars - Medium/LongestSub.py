# Given a string s, find the length of the longest
# substring without repeating characters.
#
# Constraints:
#  - 0 <= s.length <= 5 * 10^4
#  - s consists of English letters, digits, symbols and spaces.


class LongestSub(object):
    def longestSub_1(self, s):
        # pointers:
        l = 0
        r = -1  # accounts for the initial window size being empty.
        
        max_length = 0
        sub = set()
        while r < len(s) - 1:
            if s[r + 1] not in sub:
                sub.add(s[r + 1])
                r += 1  # move right pointer and expand window size
                max_length = max(max_length, r - l + 1)
            else:
                sub.remove(s[l])
                l += 1
        return max_length

ls = LongestSub()
print(ls.longestSub_1('abcabcbb'))