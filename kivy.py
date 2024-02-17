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

class MainScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)

       vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
       hl = BoxLayout()
       txt = Label(text= 'Выбери экран')
 
       vl.add_widget(ScrButton(self, direction='down', goal='first', text="1"))
       vl.add_widget(ScrButton(self, direction='left', goal='second', text="2"))
       vl.add_widget(ScrButton(self, direction='up', goal='third', text="3"))
       vl.add_widget(ScrButton(self, direction='right', goal='fourth', text="4"))
 
       hl.add_widget(txt)
       hl.add_widget(vl)
       self.add_widget(hl)

class FirstScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       btn_back = ScrButton(self, direction='up', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})
       self.add_widget(btn_back)

class SecondScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       btn_back = ScrButton(self, direction='up', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})
       self.add_widget(btn_back)

class ThirdScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       btn_back = ScrButton(self, direction='up', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})
       self.add_widget(btn_back)

class FourthScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       btn_back = ScrButton(self, direction='up', goal='main', text="Назад", size_hint=(.5, 1), pos_hint={'right': 1})
       self.add_widget(btn_back)

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
