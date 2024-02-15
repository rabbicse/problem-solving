class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in hash_map and stack:
                top = stack.pop()
                if top != hash_map[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack
        
