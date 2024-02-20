# программа с двумя экранами и одной ошибкой
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScreen(Screen):
   def __init__(self, name="first"):
      super().__init__(name=name)
      layout = BoxLayout()
      lbl = Label(text="Первый экран")
      btn = Button(text="Переключиться на экран 2")
      btn.on_press = self.next
      layout.add_widget(lbl)
      layout.add_widget(btn)
      self.add_widget(layout)

   def next(self):
      self.manager.transition.direction = 'left'
      self.manager.current = 'second'

class SecondScreen(Screen):
   def __init__(self, name="second"):
      super().__init__(name=name)
      layout = BoxLayout()
      lbl = Label(text="Второй экран")
      btn = Button(text="Переключиться на экран 1")
      btn.on_press = self.next
      layout.add_widget(lbl)
      layout.add_widget(btn)
      self.add_widget(layout)

   def next(self):
      self.manager.transition.direction = 'left'
      self.manager.current = 'first'

class MyApp(App):
   def build(self):
      sm = ScreenManager()
      sm.add_widget(FirstScreen())
      sm.add_widget(SecondScreen())
      return sm
   



app = MyApp()
app.run()
