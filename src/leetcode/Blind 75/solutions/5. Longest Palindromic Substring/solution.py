class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 0
        result = ''

        for i in range(len(s)):
            # odd length substr
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > count:
                    result = s[left:right + 1]
                    count = right - left + 1
                left -= 1
                right += 1

            # even length substr
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > count:
                    result = s[left:right + 1]
                    count = right - left + 1
                left -= 1
                right += 1
        return result
