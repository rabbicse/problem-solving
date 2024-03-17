class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        increasing = 0
        decreasing = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] >= 0:
                increasing += 1
            if nums[i] - nums[i - 1] <= 0:
                decreasing += 1

        return increasing == n - 1 or decreasing == n - 1

        
