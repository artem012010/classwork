import pygame
pygame.init()


background = (200, 255, 255)
window = pygame.display.set_mode((500, 500))
window.fill(background)

class Sprite():
    def __init__(self,filename=None, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = background
        self.image = pygame.image.load(filename)

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def colliderect(self, rect):
        return self.rect.colliderect(rect) 

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = Sprite('ball.png', 160, 200, 50, 50)
platform = Sprite('platform.png', 200, 300, 100, 30)

monsters = []
count = 9
for j in range(3):
    y = 5 + (55 * j) 
    x = 5 + (27.5 * j) 
    for i in range (count):
        monster = Sprite('enemy.png',x, y, 50, 50)
        monsters.append(monster)
        x = x + 55
    count = count - 1

clock = pygame.time.Clock()

game = True
while game:
    ball.fill()
    platform.fill()

    for monster in monsters:
        monster.draw()

    ball.draw()
    platform.draw()

    pygame.display.update()
    clock.tick(40)
