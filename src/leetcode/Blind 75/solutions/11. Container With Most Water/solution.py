class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            width = right - left
            result = max(result, min(height[left], height[right]) * width)

            # if left is less than right height then move pointer to right
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result
        
