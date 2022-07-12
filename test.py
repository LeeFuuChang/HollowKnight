import pygame
pygame.init()

window = pygame.display.set_mode((3000, 3000), pygame.FULLSCREEN)

while(True):
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            break

    window.fill((0, 0, 0))

    pygame.draw.rect(
        window, (255, 0, 0), pygame.Rect(
            0, 0, 300, 300
        )
    )

    pygame.display.update()