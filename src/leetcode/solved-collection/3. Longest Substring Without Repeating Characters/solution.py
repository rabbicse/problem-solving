class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        result = 0

        for i in range(n):
            visited = [False for i in range(256)]
            for j in range(i, n):
                if visited[ord(s[j])]:
                    break
                else:
                    result = max(j - i + 1, result)
                    visited[ord(s[j])] = True
        return result
