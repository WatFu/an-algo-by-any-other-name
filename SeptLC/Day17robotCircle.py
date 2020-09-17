class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        
        x = 0
        y = 0
        
        for letter in instructions:
            if letter == 'G':
                if direction == 0:
                    y += 1
                if direction == 1:
                    x += 1
                if direction == 2:
                    y -= 1
                if direction == 3:
                    x -= 1
            elif letter == 'L':
                direction = (direction - 1)%4
            elif letter == 'R':
                direction = (direction + 1)%4
        
        if (x == 0 and y == 0) or direction != 0:
            return True
        return False
