import kivy
kivy.require('1.11.1')
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def funcSelf(x):
    print('funcSelf')

Button.funcSelf = funcSelf


class MinhaTela(BoxLayout):
    def funcRoot(self):
        print('funcRoot')
       
        
class Estudo5App(App):
    def funcApp(self):
        print('funcApp')

janela = Estudo5App()
Window.size = 300,300
janela.run()
