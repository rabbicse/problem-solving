class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [n ** 2 for n in nums]
        res.sort()

        return res
