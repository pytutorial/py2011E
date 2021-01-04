# VD3
# Chuyển động của robot theo chương trình
class Direction:
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    
class Action:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance
        
class Robot:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0

    def moveLeft(self, d):
        self.x -= d

    def moveRight(self, d):
        self.x += d

    def moveUp(self, d):
        self.y -= d

    def moveDown(self, d):
        self.y += d

    def move(self, actionList):
        for action in actionList:
            if action.direction == Direction.LEFT:
                self.moveLeft(action.distance)
                
            elif action.direction == Direction.RIGHT:
                self.moveRight(action.distance)
                
            elif action.direction == Direction.UP:
                self.moveUp(action.distance)
                
            elif action.direction == Direction.DOWN:
                self.moveDown(action.distance)

robot = Robot(0,0)
actionList = [
    Action(Direction.LEFT, 5),
    Action(Direction.UP, 10),
    Action(Direction.RIGHT, 10),
    Action(Direction.DOWN, 20),
]
robot.move(actionList)
print(robot.x, robot.y)
