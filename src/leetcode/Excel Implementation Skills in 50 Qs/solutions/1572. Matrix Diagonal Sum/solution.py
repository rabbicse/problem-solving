class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)        
        total = 0

        for i in range(n):
            total += mat[i][i]

            k = n - i - 1
            if k != i:
                total += mat[i][k]

        return total 
        
