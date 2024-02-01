#Подключение нужных модулей
import pygame
pygame.init()
#создание окна игры
clock = pygame.time.Clock()
background_color = (255, 255, 0) #цвет фона 
window = pygame.display.set_mode((500, 500)) #окно программы 
window.fill(background_color)

class Sprite():
   def __init__(self, x, y, width, height):
       self.rect = pygame.Rect(x, y, width, height)

   #установить текст
   def set_text(self, text, font_size):
       self.text = text
       self.label = pygame.font.Font(None, font_size).render(text, True, (255,255,255))
      
   #отрисовка прямоугольника с текстом
   def draw(self):
       pygame.draw.rect(window,(0,0,0), self.rect)
       window.blit(self.label, (self.rect.x, self.rect.y + 30)) 

question_card = Sprite(100,100,300,100)  
question_card.set_text('ВОПРОС',50)
answer_card = Sprite(100,300,300,100)  
answer_card.set_text('Ответ',50)

while True:
    pygame.display.update()
    question_card.draw()
    answer_card.draw()
    clock.tick(40)           
