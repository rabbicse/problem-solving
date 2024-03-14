class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)

        for ch in t:
            if ch not in counter or counter[ch] == 0:
                return False
            else:
                counter[ch] -= 1

        return False if any(v for v in counter.values() if v > 0) else True
