class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            n = target - num
            if n in hash_map:
                return [index, hash_map[n]]

            hash_map[num] = index
        return result 
        
