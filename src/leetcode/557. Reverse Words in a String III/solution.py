class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        li = []
        for a in arr:
            li.append(a[::-1])

        return ' '.join(li)
