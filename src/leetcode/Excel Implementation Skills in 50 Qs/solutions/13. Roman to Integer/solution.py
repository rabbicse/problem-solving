class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)
        i = 0
        while i < n:
            if i + 1 < n and hash_map[s[i]] < hash_map[s[i + 1]]:
                total += hash_map[s[i + 1]] - hash_map[s[i]]
                i += 2
            else:
                total += hash_map[s[i]]
                i += 1
        return total
        
