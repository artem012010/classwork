import pygame
pygame.init()

background = (200,255,255)
window = pygame.display.set_mode((500, 500))
window.fill(background)
clock = pygame.time.Clock()


move_right = False
move_left = False
game = True


class Sprite():
    def __init__(self, filename, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(filename)

    def fill(self):
        pygame.draw.rect(window, background, self.rect)
    
    def draw(self):
        pygame.draw.rect(window, background, self.rect)  
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    
ball = Sprite('ball.png', 160, 200, 50, 50)
platform = Sprite('platform.png', 200, 300, 100, 30)



monsters = list()
count = 9
for j in range(3):
  y = 5 + (55 * j)
  x = 5 + (27.5 * j)
  for i in range(count):
      monster = Sprite('enemy.png',x, y, 50, 50)
      monsters.append(monster)
      x = x + 55
  count = count - 1

while game:

    ball.fill()
    platform.fill()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    if move_right:
        platform.rect.x += 5
    if move_left:
        platform.rect.x -= 5


    for monster in monsters:
        monster.draw()

    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(40)
