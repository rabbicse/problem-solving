class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_length = len(word1)
        word2_length = len(word2)

        l1 = 0
        l2 = 0

        result = ''
        while l1 < word1_length or l2 < word2_length:
            if l1 < word1_length:
                result += word1[l1]
                l1 += 1

            if l2 < word2_length:
                result += word2[l2]
                l2 += 1

        return result
