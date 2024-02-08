import pygame
pygame.init()

background = (200,255,255)
window = pygame.display.set_mode((500, 500))
window.fill(background)
clock = pygame.time.Clock()


move_right = False
move_left = False
speed_x = 3
speed_y = 3
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
for j in range(1):
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

    ball.rect.x += speed_x
    ball.rect.y += speed_y
  
    if  ball.rect.y < 0:
        speed_x *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1
    if ball.rect.colliderect(platform.rect):
        speed_y *= -1
    if ball.rect.y > 350:
        break

    for monster in monsters:
        monster.draw()
        if monster.rect.colliderect(ball.rect):
            monsters.remove(monster)
            monster.fill()
            speed_y *= -1
    
    if len(monsters) == 0:
        break

    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(40)
