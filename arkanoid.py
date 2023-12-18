import pygame
pygame.init()

background = (200, 255, 255)
window = pygame.display.set_mode((500, 500))
window.fill(background)

class Picture():
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

ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', 200, 300, 100, 30)

monsters = []
count = 9
for j in range(3):
    y = 5 + (55 * j)
    x = 5 + (27.5 * j)
    for i in range (count):
        m = Picture('enemy.png',x, y, 50, 50)
        monsters.append(m)
        x = x + 55
    count = count - 1

clock = pygame.time.Clock()

ball_speedx = 3
ball_speedy = 3

while True:
    ball.fill()
    platform.fill()

    ball.rect.x += ball_speedx
    ball.rect.y += ball_speedy

    if ball.rect.colliderect(platform.rect):
        ball_speedy *= -1
    if ball.rect.y < 0:
        ball_speedy *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        ball_speedx *= -1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                platform.rect.x += 20
            if event.key == pygame.K_LEFT:
                platform.rect.x -= 20

    for monster in monsters:
        monster.draw()

    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)
