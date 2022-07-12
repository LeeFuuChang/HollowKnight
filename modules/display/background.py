import pygame

class DisplayBackground:
    def __init__(self, baseImage):
        self.baseImage = baseImage

    def getView(self, left, top, width, height):
        baseImage = self.baseImage.crop((left, top, left+width, top+height))
        baseImage = pygame.image.fromstring(baseImage.tobytes(), baseImage.size, baseImage.mode)
        return baseImage