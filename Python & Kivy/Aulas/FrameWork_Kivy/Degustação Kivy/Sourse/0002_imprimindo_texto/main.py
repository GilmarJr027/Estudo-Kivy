#coding: utf-8
from kivy.app import App
from kivy.uix.label import Label

def build():
    
    lbl_text = Label()
    lbl_text.text='Curso de Python e Kivy'
    lbl_text.italic=True
    lbl_text.font_size=50
    return lbl_text
   
iniciar = App()
iniciar.build = build
iniciar.run()
