class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)

        for s in strs:
            group_dict[tuple(sorted(s))].append(s)

        return group_dict.values()
        
