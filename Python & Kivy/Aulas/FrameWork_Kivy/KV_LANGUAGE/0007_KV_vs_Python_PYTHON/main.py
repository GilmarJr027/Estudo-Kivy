import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class TelaInicial(BoxLayout):

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(TelaPos())

class TelaPos(BoxLayout):

    def on_press_bt2(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(TelaInicial())

class KVvsPY2(App):

    def build(self):
        return TelaInicial()
        
janela = KVvsPY2()
janela.run()
    



