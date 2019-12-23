from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class RootApp(FloatLayout):
    pass

class MeuApp(App):  

    def build(self):

        return RootApp()


janela_app = MeuApp()
Window.size = 300,300
janela_app.run()

