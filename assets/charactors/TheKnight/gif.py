import pygame
import time


class SpriteImage(pygame.sprite.Sprite):
    def __init__(self, fromImage=None, fromPath=None):
        pygame.sprite.Sprite.__init__(self)

        assert (fromImage is not None) or (fromPath is not None)

        if fromImage:
            self.image = fromImage
        elif fromPath:
            self.image = pygame.image.load(fromPath)



    def update(self):
        pass


class ImageGroup:
    def __init__(self, images, startAt, loopFrom, loopTo):
        self.images = images
        self.startAt = startAt
        self.loopFrom = loopFrom
        self.loopTo = loopTo
        self.now = self.startAt
        self.looping = False


    def get(self):
        return self.images[self.now]


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



imageIds1 = [
    264, 
    265, 
    266, 
    267, 
]
group = ImageGroup(
    images = [
        SpriteImage(
            pygame.image.load(
                f".\\{idx}.png"
            )
        ) for idx in imageIds1
    ], 
    startAt = 0,
    loopFrom = 0,
    loopTo = len(imageIds1) - 1
)



window = pygame.display.set_mode((128, 256))

gap = 0.08

fct = 0
fps = 60
FME = pygame.time.Clock().tick

while(True):
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            break

    window.fill((0, 0, 0))

    if fct/fps >= gap:
        fct = 0
        group.next()

    window.blit(
        group.get().image, (0, 0)
    )


    fct += 1
    FME(fps)
    pygame.display.update()