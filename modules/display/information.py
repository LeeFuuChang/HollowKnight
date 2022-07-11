from .. import const
import pygame
pygame.font.init()

class Information:
    my_font = pygame.font.SysFont('Comic Sans MS', const.game.INFORMATION_FONT_SIZE)
    def renderText(self, text):
        textSurface = self.my_font.render(text, False, (255, 255, 255))
        textWidth, textHeight = self.my_font.size(text)
        return textSurface, textWidth, textHeight

    def render(self, game, textlines):
        for i in range(len(textlines)):
            game.window.blit(
                self.renderText(textlines[i])[0],
                (0, i*const.game.INFORMATION_LINE_HEIGHT)
            )