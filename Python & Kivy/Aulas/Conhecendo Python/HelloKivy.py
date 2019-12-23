import kivy 

from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button

kivy.require('1.9.1')

class PrimeiroApp(App):
    def build(self):
        return Label(text='Hello Word! , Kivy')
    def build(self):
        return Label(text='Nome de Usuário:')
if __name__=='__main__':
    PrimeiroApp().run()
