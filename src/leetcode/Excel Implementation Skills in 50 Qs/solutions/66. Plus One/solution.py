class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        right = len(digits) - 1

        while right >= 0:
            if digits[right] == 9:
                digits[right] = 0
                right -= 1
            else:
                digits[right] += 1
                return digits

        return [1] + digits
