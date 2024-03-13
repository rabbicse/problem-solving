class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
        len_haystack = len(haystack)
        len_needle = len(needle)

        if len_haystack < len_needle:
            return -1

        for window in range(len_haystack - len_needle + 1):
            sub_str = haystack[window:window + len_needle]
            if sub_str == needle:
                return window
            
        return -1
        
