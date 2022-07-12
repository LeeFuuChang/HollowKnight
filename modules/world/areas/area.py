from ... import display
from ... import const
from ... import util
from .. import parts
from PIL import Image
import pygame
import json
import os

class Area:
    dataPath = os.path.join(os.path.dirname(__file__), "..", "data")
    def __init__(self, areaID):
        self.areaID = areaID
        self.playerBoundaries = []
        self.cameraBoundaries = []
        self.damageCollidebox = []
        self.breakableRects = []
        self.loadData(self.areaID)
        self.background = display.DisplayBackground(
            baseImage = Image.open(os.path.join(
                const.path.ASSETS_PATH, "levelBackgrounds", f"{self.areaID}.jpg"
            ))
        )





    def update__breakableRects(self, player):
        for rect in self.breakableRects:
            rect.update(player=player)
            if rect.durabilityNow == 0: self.breakableRects.remove(rect)

    def update(self, player):
        self.update__breakableRects(player=player)





    def loadData__playerBoundaries(self, areaID):
        self.playerBoundaries = []
        with open(os.path.join(self.dataPath, f"{areaID}", "playerBoundaries.json"), "r") as f:
            data = json.load(f)
            for line in data:
                self.playerBoundaries.append(
                    parts.playerBoundary.__getattribute__(f"Line{line[0]}")(
                        p1=util.classes.Vec2(line[1][0], line[1][1]),
                        p2=util.classes.Vec2(line[2][0], line[2][1]),
                        force=util.classes.Vec2(line[3][0], line[3][1]),
                    )
                )

    def loadData__cameraBoundaries(self, areaID):
        self.cameraBoundaries = []
        with open(os.path.join(self.dataPath, f"{areaID}", "cameraBoundaries.json"), "r") as f:
            data = json.load(f)
            for rect in data:
                self.cameraBoundaries.append(
                    parts.CameraBoundingBox(directions=rect[0], 
                        pTL=util.classes.Vec2(rect[1][0], rect[1][1]), 
                        pBR=util.classes.Vec2(rect[2][0], rect[2][1])
                    )
                )

    def loadData__damageCollidebox(self, areaID):
        self.damageCollidebox = []
        with open(os.path.join(self.dataPath, f"{areaID}", "damageBoxes.json"), "r") as f:
            data = json.load(f)
            for rect in data:
                self.damageCollidebox.append(
                    parts.DamageCollidebox(
                        pTL=util.classes.Vec2(rect[0][0], rect[0][1]), 
                        pBR=util.classes.Vec2(rect[1][0], rect[1][1]),
                        damageAmount=rect[2][0],
                        respawnType=rect[2][1]
                    )
                )

    def loadData__breakableRects(self, areaID):
        self.breakableRects = []
        with open(os.path.join(self.dataPath, f"{areaID}", "breakableRects.json"), "r") as f:
            data = json.load(f)
            for rect in data:
                self.breakableRects.append(
                    parts.playerBoundary.BreakableRect(
                        pTL=util.classes.Vec2(rect[0][0], rect[0][1]), 
                        pBR=util.classes.Vec2(rect[1][0], rect[1][1]),
                        durability=rect[2]
                    )
                )

    def loadData(self, areaID):
        self.loadData__playerBoundaries(areaID=areaID)
        self.loadData__cameraBoundaries(areaID=areaID)
        self.loadData__damageCollidebox(areaID=areaID)
        self.loadData__breakableRects(areaID=areaID)





    def drawLevelLines__draw(self, lines, window, cameraWorldPos, color):
        for line in lines:
            line = line - cameraWorldPos
            pygame.draw.line(
                window, color, 
                (line.p1.x, line.p1.y), 
                (line.p2.x, line.p2.y)
            )

    def drawLevelLines__playerBoundaries(self, window, cameraWorldPos, color):
        self.drawLevelLines__draw(lines=self.playerBoundaries, window=window, cameraWorldPos=cameraWorldPos, color=color)

    def drawLevelLines__cameraBoundaries(self, window, cameraWorldPos, color):
        self.drawLevelLines__draw(lines=self.cameraBoundaries, window=window, cameraWorldPos=cameraWorldPos, color=color)

    def drawLevelLines__damageCollidebox(self, window, cameraWorldPos, color):
        self.drawLevelLines__draw(lines=self.damageCollidebox, window=window, cameraWorldPos=cameraWorldPos, color=color)

    def drawLevelLines__breakableRects(self, window, cameraWorldPos, color):
        self.drawLevelLines__draw(lines=self.breakableRects, window=window, cameraWorldPos=cameraWorldPos, color=color)

    def drawLevelLines(self, window, cameraWorldPos, color):
        self.draw__playerBoundaries(window=window, cameraWorldPos=cameraWorldPos, color=color)
        self.draw__cameraBoundaries(window=window, cameraWorldPos=cameraWorldPos, color=color)
        self.draw__damageCollidebox(window=window, cameraWorldPos=cameraWorldPos, color=color)
        self.draw__breakableRects(window=window, cameraWorldPos=cameraWorldPos, color=color)