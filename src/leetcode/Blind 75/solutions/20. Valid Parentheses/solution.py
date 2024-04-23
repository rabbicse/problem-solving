"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for ch in s:
            if stack and ch in hash_map:
                item = stack.pop()
                if item != hash_map[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
