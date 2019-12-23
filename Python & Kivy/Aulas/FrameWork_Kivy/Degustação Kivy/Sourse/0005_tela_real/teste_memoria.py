from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


def build():

  
    #escopo da função
    layout = FloatLayout()
    #global pass
    
    txt_texto = TextInput()
    layout.add_widget(txt_texto)
    txt_texto.size_hint = None, None
    txt_texto.height = 30
    txt_texto.width = 150
    txt_texto.x = 150
    txt_texto.y = 150
    
    lbl_texto = Label()
    layout.add_widget(lbl_texto)
    lbl_texto.text = 'Insira seu Nome:'
    

    return layout


janela = App()
janela.build = build
from kivy.core.window import Window
Window.size= 600,600
janela.run()