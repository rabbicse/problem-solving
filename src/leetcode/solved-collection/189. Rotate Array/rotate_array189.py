class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        ans = nums.copy()
        for i in range(l):
            nums[(i + k) % l] = ans[i]
