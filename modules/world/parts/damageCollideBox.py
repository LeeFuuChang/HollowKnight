from . import playerBoundary
from ... import util



class DamageCollidebox:
    def __init__(self, pTL, pBR, damageAmount, respawnType):
        self.x1 = pTL[0]
        self.x2 = pBR[0]
        self.y1 = pTL[1]
        self.y2 = pBR[1]
        self.pTL = pTL
        self.pBR = pBR
        self.lines = [
            playerBoundary.LineU(
                p1=util.classes.Vec2(self.x1, self.y1), 
                p2=util.classes.Vec2(self.x2, self.y1), 
                force=util.classes.Vec2.zero()
            ),
            playerBoundary.LineD(
                p1=util.classes.Vec2(self.x1, self.y2), 
                p2=util.classes.Vec2(self.x2, self.y2), 
                force=util.classes.Vec2.zero()
            ),
            playerBoundary.LineL(
                p1=util.classes.Vec2(self.x1, self.y1), 
                p2=util.classes.Vec2(self.x1, self.y2), 
                force=util.classes.Vec2.zero()
            ),
            playerBoundary.LineR(
                p1=util.classes.Vec2(self.x2, self.y1), 
                p2=util.classes.Vec2(self.x2, self.y2), 
                force=util.classes.Vec2.zero()
            )
        ]
        self.damageAmount = damageAmount
        self.respawnType = respawnType


    def collideWithPoint(self, point):
        return (
            self.x1 <= point[0] and point[0] <= self.x2) and (
            self.y1 <= point[1] and point[1] <= self.y2)
