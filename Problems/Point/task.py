class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def dist(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** (1 / 2)