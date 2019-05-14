class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getDistance(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return (dx**2 + dy**2)**0.5
