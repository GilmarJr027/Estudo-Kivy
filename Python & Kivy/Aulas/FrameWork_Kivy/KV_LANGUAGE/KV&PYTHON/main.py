import kivy
kivy.require('1.11.1')
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):
    def clique(self):
        print('Oi')
        self.ids.lb1.text = ('')
        self.ids.lb2.text = ('10')
        
class Estudo4App(App):
    pass 

janela = Estudo4App()
Window.size = 300,300
janela.run()
