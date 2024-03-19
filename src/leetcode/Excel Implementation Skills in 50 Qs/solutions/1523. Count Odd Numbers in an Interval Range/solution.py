class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = 0
        start = low if low % 2 == 1 else low + 1
        end = high if high % 2 == 1 else high - 1
        
        return 0 if start > end else ((end - start) // 2) + 1
