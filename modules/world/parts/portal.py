from . import playerBoundary
from ... import util



class portalRect:
    def __init__(self, pTL, pBR, portalID, destAreaID, destPortalID, arriveStiky):
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
        self.portalID = portalID
        self.destAreaID = destAreaID
        self.destPortalID = destPortalID
        self.arriveStiky = arriveStiky



    def getArrivePosition(self, targetCollideboxOffset, targetCollideboxSize):
        x, y = 0, 0
        if self.arriveStiky[0]==self.arriveStiky[1]:
            y = round((self.y1+self.y2-targetCollideboxSize[1])/2)-targetCollideboxOffset[1]
        elif self.arriveStiky[0]:
            y = self.y1
        elif self.arriveStiky[1]:
            y = self.y2-targetCollideboxSize[1]-targetCollideboxOffset[1]
        if self.arriveStiky[2]==self.arriveStiky[3]:
            x = round((self.x1+self.x2-targetCollideboxSize[0])/2)-targetCollideboxOffset[0]
        elif self.arriveStiky[2]:
            x = self.x1
        elif self.arriveStiky[3]:
            x = self.x2-targetCollideboxSize[0]-targetCollideboxOffset[0]
        return (x, y)
        


    def collideWithPoint(self, point):
        return (
            self.x1 <= point[0] and point[0] <= self.x2) and (
            self.y1 <= point[1] and point[1] <= self.y2)



    def update(self, player):
        playerPTL = (player.position.x + player.collideboxOffsetX, player.position.y + player.collideboxOffsetY)
        playerPBR = (playerPTL[0] + player.collideboxWidth, playerPTL[1] + player.collideboxHeight)
        points = [
            playerPTL, (playerPBR[0], playerPTL[1]),
            (playerPTL[0], playerPBR[1]), playerPBR
        ]
        for vertex in points:
            if self.collideWithPoint(point=vertex):
                return True
        return False