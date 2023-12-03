import pygame
pygame.init()

game_over = False

platform_x = 200
platform_y = 330

speed_x = 3
speed_y = 3

move_right = False
move_left = False
move_up = False
move_down = False

start_x = 5
start_y = 5

count = 9
monsters = []

point = 0

back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()


class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height)
      self.fill_color = back

  def fill(self):
      pygame.draw.rect(mw, self.fill_color, self.rect)   

  def colliderect(self, rect):
      return self.rect.colliderect(rect)

class Label(Area):

  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
      
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Picture(Area):
    
  def __init__(self, filename, x=0, y=0, width=10, height=10):
      Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
      self.image = pygame.image.load(filename)

  def draw(self):
      mw.blit(self.image, (self.rect.x, self.rect.y))

ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', platform_x, platform_y, 100, 30)


count = 9
monsters = []
for j in range(3):
  y = start_y + (55 * j) 
  x = start_x + (27.5 * j) 
  for i in range (count):
      d = Picture('enemy.png',x, y, 50, 50)
      monsters.append(d)
      x = x + 55
  count = count - 1

while not game_over:
  
  ball.fill()
  platform.fill()

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          game_over = True
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT: #если нажата клавиша
              move_right = True #поднимаем флаг
          if event.key == pygame.K_LEFT:
              move_left = True #поднимаем флаг
          if event.key == pygame.K_UP: #если нажата клавиша
              move_up = True #поднимаем флаг
          if event.key == pygame.K_DOWN:
              move_down = True #поднимаем флаг
      elif event.type == pygame.KEYUP:
          if event.key == pygame.K_RIGHT:
              move_right = False #опускаем флаг
          if event.key == pygame.K_LEFT:
              move_left = False #опускаем флаг
          if event.key == pygame.K_UP:
              move_up = False #опускаем флаг
          if event.key == pygame.K_DOWN:
              move_down = False #опускаем флаг
      
    
  if move_right: #флаг движения вправо
      platform.rect.x += 6
  if move_left: #флаг движения влево
      platform.rect.x -= 6
  if move_up: 
      platform.rect.y -= 6
  if move_down: 
      platform.rect.y += 6


  ball.rect.x += speed_x
  ball.rect.y += speed_y

  if ball.colliderect(platform.rect):
    speed_y *= -1

  if ball.rect.y < 0:
    speed_y *= -1

  if ball.rect.x < 0 or ball.rect.x > 450:
    speed_x *= -1

  if ball.rect.y > 450:
      lose = Label(150,150,50,50,back)
      lose.set_text('Вай лашара',60,(255,0,0))
      lose.draw(10,10)
      game_over = True

  platform.draw()
  ball.draw()

  for m in monsters:
      m.draw()
      if m.colliderect(ball.rect):
          point += 1
          monsters.remove(m)
          m.fill()
          speed_y *= -1

  if len(monsters) == 0:
      lose = Label(150,150,50,50,back)
      lose.set_text('Вай красава',60,(0,255,0))
      lose.draw(10,10)
      game_over = True


  pygame.display.update()
  clock.tick(40)
