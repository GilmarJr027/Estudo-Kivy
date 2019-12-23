#coding: utf-8
from kivy.app import App
from kivy.uix.button import Button

def click():
    print('O botão foi clicado!')

def build():
    btn_sair = Button()
    btn_sair.text='Sair'
    btn_sair.italic=True
    btn_sair.font_size=25
    #função on_press se encarrega a saber se o evento clique veio de um mouse ou tela de toque
    btn_sair.on_press = click
    return btn_sair
app = App()
app.build = build
app.run()
