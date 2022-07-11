from .colliders.linear import LinearCollider
from .vector import Vec2


class Line:
    collider = LinearCollider
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.isHorizontal = (self.y1==self.y2)
        self.isVertical = (self.x1==self.x2)
        if self.isHorizontal or self.isVertical:
            if x1 > x2 or y1 > y2:
                self.x1, self.x2 = self.x2, self.x1
                self.y1, self.y2 = self.y2, self.y1
        self.p1 = Vec2(self.x1, self.y1)
        self.p2 = Vec2(self.x2, self.y2)


    def add(self, other):
        self.p1.add(other)
        self.p2.add(other)

    def __add__(self, other):
        return self.__class__(
            self.p1.x+other[0], self.p1.y+other[1],
            self.p2.x+other[0], self.p2.y+other[1]
        )


    def sub(self, other):
        self.p1.sub(other)
        self.p2.sub(other)

    def __sub__(self, other):
        return self.__class__(
            self.p1.x-other[0], self.p1.y-other[1],
            self.p2.x-other[0], self.p2.y-other[1]
        )


    def checkCollided(self, *args):
        """
        1 arg => line\n
        2 arg => p1, p2\n
        4 arg => x1, y1, x2, y2\n
        """
        if len(args) == 1:
            return self.collider.checkCollided(
                self.p1, self.p2, args[0].p1, args[0].p2
            )
        elif len(args) == 2:
            return self.collider.checkCollided(
                self.p1, self.p2, args[0], args[1]
            )
        elif len(args) == 4:
            return self.collider.checkCollided(
                self.p1, self.p2, (args[0], args[1]), (args[2], args[3])
            )