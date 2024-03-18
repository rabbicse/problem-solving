class Solution:
    def isRobotBounded(self, instructions: str) -> bool:        
        # north = 0, south = 1, east = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = y = 0
        # facing north
        idx = 0

        for instruction in instructions:
            if instruction == 'L':
                idx = (idx + 3) % 4 
            elif instruction == 'R':
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

        return (x == 0 and y == 0) or idx != 0             
        
