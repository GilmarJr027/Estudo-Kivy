from kivy.app import App
from kivy.uix.textinput import TextInput


def build():

    txt_nome = TextInput()
    return txt_nome


janela = App()
janela.build = build
janela.run()