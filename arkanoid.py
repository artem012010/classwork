import pygame
pygame.init()

background = (200,255,255)
window = pygame.display.set_mode((500, 500))
window.fill(background)
clock = pygame.time.Clock()


while True:
    pygame.display.update()
    clock.tick(40)
