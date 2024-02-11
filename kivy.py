# кнопка и надпись подписываются на события
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

def tst():
    print('KUKU!')

class MyApp(App):
    def build(self):
        txt = Label(text='Это надпись')
        btn = Button(text='Это кнопка')
        btn.on_press = tst 
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout

MyApp().run() # проверяйте, что будет печататься при кликах по кнопке и по надписи
