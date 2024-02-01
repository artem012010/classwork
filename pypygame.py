#Подключение нужных модулей
import pygame
pygame.init()
#создание окна игры
clock = pygame.time.Clock()
background_color = (255, 255, 0) #цвет фона 
window = pygame.display.set_mode((500, 500)) #окно программы 
window.fill(background_color)

while True:
    pygame.display.update()
    clock.tick(40)           
