class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(s)

        for ch in t:
            if ch not in counter or counter[ch] == 0:
                return ch
            else:
                counter[ch] -= 1
