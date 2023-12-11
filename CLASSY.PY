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
        window.blit(self.text,(self.rectangle.x,self.rectangle.y))

card_question = Card(20,50,300,80)
card_answer = Card(20,150,300,80)
card_question.set_text('ВОПРОС')
card_answer.set_text('ОТВЕТ')

while True:
    pygame.display.update()

    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint(1,3)
                if num == 1:
                    card_question.set_text('Почем он а не я')
                if num == 2:
                    card_question.set_text('Почем небо голубое')
                if num == 3:
                    card_question.set_text('Почем трава зеленая')
                
            if event.key == pygame.K_a:
                num = randint(1,3)
                if num == 1:
                    card_answer.set_text('Потому что')
                if num == 2:
                    card_answer.set_text('Так надо')
                if num == 3:
                    card_answer.set_text('Гномики покрасили')

    card_question.draw()
    card_answer.draw()
    clock.tick(30)
