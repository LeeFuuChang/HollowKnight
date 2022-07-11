class LinearCollider:
    @staticmethod
    def checkCollided(p1, p2, p3, p4):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        x3, y3 = p3[0], p3[1]
        x4, y4 = p4[0], p4[1]
        uD = ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
        uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / (uD if uD else 1)
        uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / (uD if uD else 1)
        if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
            intersectionX = x1 + (uA * (x2-x1))
            intersectionY = y1 + (uA * (y2-y1))
            return (True, intersectionX, intersectionY)
        return (False, None, None)