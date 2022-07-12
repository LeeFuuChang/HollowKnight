from . import playerBoundaryU
from . import playerBoundaryD
from . import playerBoundaryL
from . import playerBoundaryR
from .... import const
from .... import util
from .... import time



class BreakableRect:
    invulnerableTimer = time.Timer(const.world.PLAYER_BOUNDARY_BREAKABLE_INVULNERABLE_DURATION)

    def __init__(self, pTL, pBR, durability):
        self.isInvulnerable = False
        self.x1 = pTL[0]
        self.x2 = pBR[0]
        self.y1 = pTL[1]
        self.y2 = pBR[1]
        self.pTL = pTL
        self.pBR = pBR
        self.lines = [
            playerBoundaryU.LineU(
                p1=util.classes.Vec2(self.x1, self.y1), 
                p2=util.classes.Vec2(self.x2, self.y1), 
                force=util.classes.Vec2.zero()
            ),
            playerBoundaryD.LineD(
                p1=util.classes.Vec2(self.x1, self.y2), 
                p2=util.classes.Vec2(self.x2, self.y2), 
                force=util.classes.Vec2.zero()
            ),
            playerBoundaryL.LineL(
                p1=util.classes.Vec2(self.x1, self.y1), 
                p2=util.classes.Vec2(self.x1, self.y2), 
                force=util.classes.Vec2.zero()
            ),
            playerBoundaryR.LineR(
                p1=util.classes.Vec2(self.x2, self.y1), 
                p2=util.classes.Vec2(self.x2, self.y2), 
                force=util.classes.Vec2.zero()
            )
        ]
        self.durabilityNow = durability
        self.durabilityMax = durability


    def update(self, player):
        if not self.isInvulnerable:
            for attackDamageBoxPTL, attackDamageBoxPBR in player.damageBoxes.attack:
                if not util.functions.rectCollideWithRect(
                    Rect1PTL=attackDamageBoxPTL, Rect2PTL=self.pTL,
                    Rect1PBR=attackDamageBoxPBR, Rect2PBR=self.pBR,
                ): continue
                self.invulnerableTimer.reset()
                self.isInvulnerable = True
                self.durabilityNow = max(self.durabilityNow-1, 0)
                # print("hit", self.durabilityNow)
        elif self.invulnerableTimer.check(autoReset=False):
            self.isInvulnerable = False


    def collideWithPoint(self, point):
        return (
            self.x1 <= point[0] and point[0] <= self.x2) and (
            self.y1 <= point[1] and point[1] <= self.y2)
