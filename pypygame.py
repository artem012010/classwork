#Подключение нужных модулей
from random import randint
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
question_card.draw()
answer_card = Sprite(100,300,300,100)  
answer_card.set_text('Ответ',50)
answer_card.draw()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                number = randint(1,3)
                if number == 1:
                    question_card.set_text('Кто самый крутой?', 30)
                if number == 2:
                    question_card.set_text('Кто здесь Гитлер?', 30)
                if number == 3:
                    question_card.set_text('Кто самый умный?', 30) 
                question_card.draw()  

            if event.key == pygame.K_a:
                number = randint(1,3)
                if number == 1:
                    answer_card.set_text('Роман', 30)
                if number == 2:
                    answer_card.set_text('Кутман', 30)
                if number == 3:
                    answer_card.set_text('АЛИЯ', 30)   
                answer_card.draw()

    clock.tick(40)           
          
