import kivy
kivy.require('1.11.1')
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


#definindo o codigo kivy dentro de um arquivo Python
code = """
BoxLayout:

    Button:
        text: "BT 1"
    Button:
        text: "BT 2"
"""

#Importando a classe Builder 
from kivy.lang import Builder
      
class EstudoApp(App):
    #Retornando o codigo kv atraves da função build
    def build(self):
        return Builder.load_string(code)

janela = EstudoApp()
Window.size = 300,300
janela.run()