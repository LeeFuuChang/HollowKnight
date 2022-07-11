from .. import const
from . import image
from .. import util
import pygame
import os


class InterfaceImages:
    def __init__(self):
        self.load()

    def load(self):
        self.GAMEPLAY_HEALTH_FRAME = image.SpriteImage(
            fromPath=os.path.join(
                const.path.ASSETS_PATH, "ui", "gameplay", "health_frame.png"
            )
        ).image
        self.GAMEPLAY_HEALTH_BLANK = image.SpriteImage(
            fromPath=os.path.join(
                const.path.ASSETS_PATH, "ui", "gameplay", "health_blank.png"
            )
        ).image
        self.GAMEPLAY_HEALTH_FULL = image.SpriteImage(
            fromPath=os.path.join(
                const.path.ASSETS_PATH, "ui", "gameplay", "health_full.png"
            )
        ).image


class Interface:
    images = InterfaceImages()
    def __init__(self, displaySize):
        self.displayWidth = displaySize[0]
        self.displayHeight = displaySize[1]

    def drawPlayerHealth(self, window, playerHealthNow, playerHealthMax):
        window.blit(
            self.images.GAMEPLAY_HEALTH_FRAME, (
                const.interface.PLAYER_HEALTH_FRAME_OFFSET_X * const.game.GAME_SIZE_RATIO,
                const.interface.PLAYER_HEALTH_FRAME_OFFSET_Y * const.game.GAME_SIZE_RATIO
            )
        )
        for i in range(playerHealthMax):
            if i >= playerHealthNow:
                window.blit(
                    self.images.GAMEPLAY_HEALTH_BLANK, (
                        (
                            const.interface.PLAYER_HEALTH_BLOCK_OFFSET_X * const.game.GAME_SIZE_RATIO
                             + int(const.interface.PLAYER_HEALTH_BLOCK_WIDTH*const.game.GAME_SIZE_RATIO/3)*i
                             + const.interface.PLAYER_HEALTH_BLOCK_WIDTH*const.game.GAME_SIZE_RATIO*(i+1)
                        ), 
                        const.interface.PLAYER_HEALTH_BLOCK_OFFSET_Y
                    )
                )
            else:
                window.blit(
                    self.images.GAMEPLAY_HEALTH_FULL, (
                        (
                            const.interface.PLAYER_HEALTH_BLOCK_OFFSET_X * const.game.GAME_SIZE_RATIO
                             + int(const.interface.PLAYER_HEALTH_BLOCK_WIDTH*const.game.GAME_SIZE_RATIO/3)*i
                             + const.interface.PLAYER_HEALTH_BLOCK_WIDTH*const.game.GAME_SIZE_RATIO*(i+1)
                        ), 
                        const.interface.PLAYER_HEALTH_BLOCK_OFFSET_Y
                    )
                )