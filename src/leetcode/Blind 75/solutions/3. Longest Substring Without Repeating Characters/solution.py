class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        hash_map = {}

        left = 0
        for right in range(len(s)):
            if s[right] in hash_map:
                left = max(hash_map[s[right]], left)

            ans = max(ans, right - left + 1)
            hash_map[s[right]] = right + 1
        
        return ans
        
