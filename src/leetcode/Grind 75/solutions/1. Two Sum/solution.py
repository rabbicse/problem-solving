class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            temp = target - num
            if hash_map and temp in hash_map:
                return [i, hash_map[temp]]
            
            hash_map[num] = i
        return []
        
