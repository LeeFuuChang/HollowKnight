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
            f"",
            f"CameraMode: {self.camera.mode}",
            f"",
            f"States:",
            f"       attack: {self.player.states.attack}",
            f"       attackAvailable: {self.player.states.attackAvailable}",
            f"       knockback: {self.player.states.knockback}",
            f"       idol: {self.player.states.idol}",
            f"       run: {self.player.states.run}",
            f"       dash: {self.player.states.dash}",
            f"       dashAvailable: {self.player.states.dashAvailable}",
            f"       superDash: {self.player.states.superDash}",
            f"       jump: {self.player.states.jump}",
            f"       midAirJump: {self.player.states.midAirJump}",
            f"       midAirJumpAvailable: {self.player.states.midAirJumpAvailable}",
            f"       fall: {self.player.states.fall}",
            f"       grounded: {self.player.states.grounded}",
            f"       onCliff: {self.player.states.onCliff}",
            f"",
            f"Skill:",
            f"       dash: {self.player.skill.dash}",
            f"       midAirJump: {self.player.skill.midAirJump}",
        ])

    def run(self):
        while(True):
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT: return

            self.window.fill((255, 255, 255))

            pressedKeys = pygame.key.get_pressed()

            visibleLines = self.camera.getVisibleLines(currentLines=self.currentLevel.playerBoundaries)

            self.player.update(pressedKeys=pressedKeys, movementboundaries=visibleLines, damageBoxes=self.currentLevel.damageCollidebox)

            time.Timer.addAll()

            self.camera.update(pressedKeys=pressedKeys, boundingBoxes=self.currentLevel.cameraBoundaries)
            self.camera.draw(self.window)

            self.renderGameInformation()

            # self.currentLevel.draw(window=self.window, cameraWorldPos=self.camera.position, color=(0, 0, 255))

            self.frame(const.game.FPS)
            pygame.display.update()