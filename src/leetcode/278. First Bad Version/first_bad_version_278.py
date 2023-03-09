# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        index = -1

        while start <= end:
            mid = int((start + end) / 2)

            if isBadVersion(mid):
                index = mid
                end = mid - 1
            else:
                start = mid + 1
        return index
