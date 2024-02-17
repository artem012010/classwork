from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class ScrButton(Button):
   def __init__(self, screen, direction='right', goal='main', **kwargs):
       super().__init__(**kwargs)
       self.screen = screen
       self.direction = direction
       self.goal = goal
   def on_press(self):
       self.screen.manager.transition.direction = self.direction
       self.screen.manager.current = self.goal







class MyApp(App):
   def build(self):
       sm = ScreenManager()
       sm.add_widget(MainScr(name='main'))
       sm.add_widget(FirstScr(name='first'))
       sm.add_widget(SecondScr(name='second'))
       sm.add_widget(ThirdScr(name='third'))
       sm.add_widget(FourthScr(name='fourth'))
 
       return sm
 
MyApp().run()
