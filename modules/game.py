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
            const.game.WINDOW_DEFAULT_WIDTH, 
            const.game.WINDOW_DEFAULT_HEIGHT, 
        ), pygame.FULLSCREEN)
        self.frame = pygame.time.Clock().tick

        self.displaySize = pygame.display.get_surface().get_size()

        self.player = charactors.player.Player(displaySize=self.displaySize)

        self.camera = display.Camera(
            displaySize=self.displaySize, target=self.player
        )

        self.currentLevelID = 0
        self.currentLevel = world.areas.Area(self.currentLevelID)
        print(len(self.currentLevel.playerBoundaries))

        self.currentLines = self.currentLevel.playerBoundaries
        self.information = display.Information()





    def renderGameInformation(self):
        self.information.render(self, [
            f"XY: {self.player.position.x} / {self.player.position.y}",
            f"V: { round(self.player.velocity.x)} / {self.player.velocity.y}",
            f"CollidedLines: {self.player.collidedCount}",
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

            self.window.fill((255, 255, 255))

            pressedKeys = pygame.key.get_pressed()

            movementboundaries = [*self.currentLevel.playerBoundaries]
            for rect in self.currentLevel.breakableRects:
                movementboundaries.extend(rect.lines)
            visibleLines = self.camera.filterVisibleLines(lines=movementboundaries)

            self.player.update(pressedKeys=pressedKeys, movementboundaries=visibleLines, damageBoxes=self.currentLevel.damageCollidebox)

            time.Timer.addAll()

            self.camera.update(pressedKeys=pressedKeys, boundingBoxes=self.currentLevel.cameraBoundaries)
            self.camera.draw(self.window)

            self.renderGameInformation()

            self.currentLevel.update(player=self.player)

            self.frame(const.game.FPS)
            pygame.display.update()