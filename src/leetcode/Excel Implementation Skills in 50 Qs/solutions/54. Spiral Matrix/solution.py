class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        rows, cols = len(matrix), len(matrix[0])
        left, up = 0, 0
        right, down = cols - 1, rows - 1
        k = 0

        while k < rows * cols:
            # traverse left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])
                k+= 1

            # traverse up to down
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])
                k+= 1

            # traverse right to left
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])
                    k += 1

            # traverse down to up
            if left != right:
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])
                    k += 1

            left += 1
            right -= 1
            up += 1
            down -= 1            

        return result

        
