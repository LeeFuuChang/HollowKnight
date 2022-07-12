from .. import const
from .. import util
import pygame


class SpriteImage(pygame.sprite.Sprite):
    def __init__(self, fromImage=None, fromPath=None):
        pygame.sprite.Sprite.__init__(self)

        assert (fromImage is not None) or (fromPath is not None)

        if fromImage:
            self.image = fromImage
        elif fromPath:
            self.image = pygame.image.load(fromPath)
        self.width, self.height = self.image.get_size()


    def update(self):
        pass




class ImageGroup:
    def __init__(self, images, startAt, loopFrom, loopTo, gap=1):
        self.images = images
        self.startAt = startAt
        self.loopFrom = loopFrom
        self.loopTo = loopTo
        self.now = self.startAt
        self.looping = False
        self.gap = gap


    def getImage(self):
        return self.images[self.now].image


    def getHitbox(self):
        return self.images[self.now].hitbox


    def next(self):
        self.now += 1
        if not self.looping:
            if self.now == len(self.images):
                self.looping = True
                self.now = self.loopFrom
        else:
            if self.now == self.loopTo+1:
                self.now = self.loopFrom


    def reset(self):
        self.now = self.startAt




class NamedImageGroups:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            self.__setattr__(
                name, value
            )