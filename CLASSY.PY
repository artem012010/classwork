import pygame
pygame.init()

# Цвета для игры
background = (57, 203, 202)


#Создать и залить фон
window = pygame.display.set_mode((500,500)) 
window.fill(background)
# Обьект часов
clock = pygame.time.Clock()

while True:
    pygame.display.update()
    
    clock.tick(30)
