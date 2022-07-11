from ... import util
from .. import parts
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
        self.breakableCollidebox = []
        self.loadData(self.areaID)





    def loadData__playerBoundaries(self, areaID):
        self.playerBoundaries = []
        with open(os.path.join(self.dataPath, f"{areaID}", "playerBoundaries.json"), "r") as f:
            data = json.load(f)
            for line in data:
                self.playerBoundaries.append(
                    parts.playerBoundary.__getattribute__(
                        f"Line{line[0]}"
                    )(p1=line[1], p2=line[2], force=line[3])
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


    def loadData__breakableCollidebox(self, areaID):
        self.breakableCollidebox = []

    def loadData(self, areaID):
        self.loadData__playerBoundaries(areaID=areaID)
        self.loadData__cameraBoundaries(areaID=areaID)
        self.loadData__damageCollidebox(areaID=areaID)
        self.loadData__breakableCollidebox(areaID=areaID)





    def drawLevelLines(self, lines, window, cameraWorldPos, color):
        for line in lines:
            line = line - cameraWorldPos
            pygame.draw.line(
                window, color, 
                (line.p1.x, line.p1.y), 
                (line.p2.x, line.p2.y)
            )

    def draw__playerBoundaries(self, window, cameraWorldPos, color):
        self.drawLevelLines(lines=self.playerBoundaries, window=window, cameraWorldPos=cameraWorldPos, color=color)

    def draw__cameraBoundaries(self, window, cameraWorldPos, color):
        self.drawLevelLines(lines=self.cameraBoundaries, window=window, cameraWorldPos=cameraWorldPos, color=color)

    def draw__damageCollidebox(self, window, cameraWorldPos, color):
        self.drawLevelLines(lines=self.damageCollidebox, window=window, cameraWorldPos=cameraWorldPos, color=color)

    def draw__breakableCollidebox(self, window, cameraWorldPos, color):
        self.drawLevelLines(lines=self.breakableCollidebox, window=window, cameraWorldPos=cameraWorldPos, color=color)

    def draw(self, window, cameraWorldPos, color):
        self.draw__playerBoundaries(window=window, cameraWorldPos=cameraWorldPos, color=color)
        self.draw__cameraBoundaries(window=window, cameraWorldPos=cameraWorldPos, color=color)
        self.draw__damageCollidebox(window=window, cameraWorldPos=cameraWorldPos, color=color)
        self.draw__breakableCollidebox(window=window, cameraWorldPos=cameraWorldPos, color=color)