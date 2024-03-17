class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 2:
            return False
        
        arr.sort()
        diff = abs(arr[1] - arr[0])
        for i in range(2, n):
            if diff != abs(arr[i] - arr[i - 1]):
                return False

        return True
