class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = int((end + start) / 2)
            print(mid)

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1

        return -1
