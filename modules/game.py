from . import display
from . import const
from . import charactors
from . import time
from . import util
from . import world
import pygame


pygame.init()


class HollowKnight:
    def __init__(self):
        self.window = pygame.display.set_mode((
            const.game.GAME_WIDTH, 
            const.game.GAME_HEIGHT 
        ), pygame.FULLSCREEN)
        self.frame = pygame.time.Clock().tick

        self.displaySize = (
            const.game.GAME_WIDTH,
            const.game.GAME_HEIGHT
        )

        self.allAreas = [world.areas.Area(i) for i in range(const.world.AREAS_COUNT)]
        self.currentAreaID = 0
        self.currentArea = self.allAreas[self.currentAreaID]

        self.player = charactors.player.Player(displaySize=self.displaySize, areaID=self.currentAreaID)

        self.camera = display.Camera(
            displaySize=self.displaySize, displayOffset=(
                const.game.DISPLAY_OFFSET_X,
                const.game.DISPLAY_OFFSET_Y
            ), target=self.player
        )

        self.currentLines = self.currentArea.playerBoundaries
        self.information = display.Information()





    def renderGameInformation(self):
        self.information.render(self, [
            f"XY: {self.player.position.x} / {self.player.position.y}",
            f"V: { round(self.player.velocity.x)} / {self.player.velocity.y}",
            f"CollidedLines: {self.player.collidedCountV} V   {self.player.collidedCountH} H",
        ] + [""] + [
            f"CameraMode: {self.camera.mode}",
        ] + [""] + [
            f"States:"] + [
            f"       {name}: {self.player.states[name]}" for name in self.player.states.names
        ] + [""] + [
            f"Skill:"] + [
            f"       {name}: {self.player.skillUnlocked[name]}" for name in self.player.skillUnlocked.names
        ] + [""] + [
            f"Spell:"] + [
            f"       {name}: {self.player.spellUnlocked[name]}" for name in self.player.spellUnlocked.names
        ])

    def run(self):
        while(True):
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT: return

            self.window.fill((0, 0, 0))

            pressedKeys = pygame.key.get_pressed()

            movementboundaries = [*self.currentArea.playerBoundaries]
            for rect in self.currentArea.breakableRects:
                movementboundaries.extend(rect.lines)
            visibleLines = self.camera.filterVisibleLines(lines=movementboundaries)

            self.player.update(
                pressedKeys=pressedKeys, allAreas=self.allAreas,
                movementboundaries=visibleLines, 
                damageBoxes=self.currentArea.damageCollidebox,
                portalRects=self.currentArea.portalRects
            )
            if self.player.areaID != self.currentAreaID:
                self.currentAreaID = self.player.areaID
                self.currentArea = self.allAreas[self.currentAreaID]
                self.camera.fastChase()

            time.Timer.addAll()

            self.camera.update(boundingBoxes=self.currentArea.cameraBoundaries)
            self.camera.draw(window=self.window, currentLevel=self.currentArea)

            self.renderGameInformation()

            self.currentArea.update(player=self.player)

            self.frame(const.game.FPS)
            pygame.display.update()