class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i, op in enumerate(operations):
            if '+' in op and len(result) >= 2:
                result.append(result[-1] + result[-2])
            elif 'D' in op:
                result.append(result[-1] * 2)
            elif 'C' in op:
                result.pop()
            else:
                result.append(int(op))

        return sum(result)

        
