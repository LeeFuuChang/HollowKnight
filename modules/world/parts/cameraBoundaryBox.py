from ... import util



class CameraBoundingBox:
    def __init__(self, directions, pTL, pBR):
        self.x1 = pTL[0]
        self.x2 = pBR[0]
        self.y1 = pTL[1]
        self.y2 = pBR[1]
        self.pTL = pTL
        self.pBR = pBR
        self.directions = [int(_) for _ in directions]
        self.correctionFunctions = [
            self.getCorrectionU,
            self.getCorrectionD,
            self.getCorrectionL,
            self.getCorrectionR,
        ]


    def collideWithPoint(self, point):
        return (
            self.x1 < point[0] and point[0] < self.x2
        ) and (
            self.y1 < point[1] and point[1] < self.y2
        )


    def getCorrectionU(self, cameraPos, cameraDisplayWidth, cameraDisplayHeight):
        if cameraPos[1]+cameraDisplayHeight > self.y2:
            return util.classes.Vec2(0, self.y2 - (cameraPos[1]+cameraDisplayHeight))
        else:
            return util.classes.Vec2(0, 0)


    def getCorrectionD(self, cameraPos, cameraDisplayWidth, cameraDisplayHeight):
        if cameraPos[1] < self.y1:
            return util.classes.Vec2(0, self.y1-cameraPos[1])
        else:
            return util.classes.Vec2(0, 0)


    def getCorrectionL(self, cameraPos, cameraDisplayWidth, cameraDisplayHeight):
        if cameraPos[0]+cameraDisplayWidth > self.x2:
            return util.classes.Vec2(self.x2-(cameraPos[0]+cameraDisplayWidth), 0)
        else:
            return util.classes.Vec2(0, 0)


    def getCorrectionR(self, cameraPos, cameraDisplayWidth, cameraDisplayHeight):
        if cameraPos[0] < self.x1:
            return util.classes.Vec2(self.x1-cameraPos[0], 0)
        else:
            return util.classes.Vec2(0, 0)


    def getCorrection(self, cameraPos, cameraDisplayWidth, cameraDisplayHeight):
        correctionVector = util.classes.Vec2(0, 0)
        for i in range(4):
            if not self.directions[i]: continue
            vct = self.correctionFunctions[i](cameraPos, cameraDisplayWidth, cameraDisplayHeight)
            correctionVector.add(vct)
        return correctionVector