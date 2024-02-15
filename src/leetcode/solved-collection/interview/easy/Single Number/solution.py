class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hmap = {}
        
        for n in nums:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 1
                
        for k, v in hmap.items():
            if v == 1:
                return k
            
        return -1
