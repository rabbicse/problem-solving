class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                
