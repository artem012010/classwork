import pygame
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
question_card.set_text('Почему небо голубое')


        
while True:
    pygame.display.update()
    question_card.draw()
    clock.tick(30)
