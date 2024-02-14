class Button():
    def __init__(self, title, x, y):
        self.title = title
        self.x = x
        self.y = y
        self.appearance = True
    def hide(self ):
        self.appearance = False
    def show(self ):
        self.appearance = True
    def print_status( self):
        print('Данные о виджете:')
        print(self.title, self.x, self.y, self.appearance)

ok_button = Button('ok', 100, 100)
ok_button.print_status()
ok_button.hide()
ok_button.print_status()



class Title():
    #конструктор
    def __init__(self,text,x,y,vision):
        self.text = text
        self.x = x
        self.y = y
        self.vision = vision
    
    def info(self):
        print('Кнопка',self.text)
        print('Расположение',self.x,self.y)
        print('Видимость',self.vision)

    def off(self):
        self.vision = False
        print('Выключили кнопку')

    def on(self):
        self.vision = True
        print('Включили кнопку')

#создай две надписи
button1 = Title('Купить',-50,100,True)
button2 = Title('Продать',-50,-100,True)
#скрой вторую надпись
print('Кнопка включена?', button2.vision)
button2.off()
print('Кнопка включена?', button2.vision)
