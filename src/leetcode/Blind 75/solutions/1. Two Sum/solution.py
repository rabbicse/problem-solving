"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, val in enumerate(nums):
            temp = target - val
            if hash_map and temp in hash_map:
                return [hash_map[temp], index]
            
            hash_map[val] = index
