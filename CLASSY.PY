import pygame
from random import randint
pygame.init()

# Цвета для игры
background = (57, 203, 202)
black = (0,0,0)
white = (255,255,255)

#Создать и залить фон
window = pygame.display.set_mode((500,500)) 
window.fill(background)
# Обьект часов
clock = pygame.time.Clock()

class Card():
    def __init__(self,x,y,width,height):
        self.rectangle = pygame.Rect(x,y,width,height)

    def set_text(self,text):
        self.text = pygame.font.Font(None,50).render(text,True,white)

    def draw(self):
        pygame.draw.rect(window,black,self.rectangle)
        window.blit(self.text,(self.rectangle.x + 10,self.rectangle.y + 30))

question_card = Card(20,150,400,100)
question_card.set_text('Вопрос')

answer_card = Card(20,300,400,100)
answer_card.set_text('Ответ')

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint(1,2)
                if num == 1:
                    question_card.set_text('Почему небо голубое')
                if num == 2:
                    question_card.set_text('Почему он а не я?')

            if event.key == pygame.K_a:
                num = randint(1,2)
                if num == 1:
                    answer_card.set_text('Потому - что')
                if num == 2:
                    answer_card.set_text('Прост')

    question_card.draw()
    answer_card.draw()
    clock.tick(30)
