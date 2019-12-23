#coding: UTF-8
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout


class MeuPrograma(App):

    def build(self):
        
        layout = FloatLayout()

        lbl_hello = Label()
        layout.add_widget(lbl_hello)
        lbl_hello.text = "Hello Word"

        return layout

janela = MeuPrograma()
from kivy.core.window import Window
Window.size = 300,300
janela.run()

