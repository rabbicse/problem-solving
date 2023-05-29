class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        ans = []
        
        for n in nums1:
            if n not in hash_map:
                hash_map[n] = 1 
            else:
                hash_map[n] = hash_map[n] + 1
                
        for n in nums2:
            if n in hash_map and hash_map[n] > 0:
                hash_map[n] = hash_map[n] - 1
                ans.append(n)
                
        return ans
