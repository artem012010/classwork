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
