import math

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceTo(self, city):
        xDistance = abs(self.getX() - city.getX())
        yDistance = abs(self.getY() - city.getY())
        distance = math.sqrt(xDistance**2 + yDistance**2)
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
