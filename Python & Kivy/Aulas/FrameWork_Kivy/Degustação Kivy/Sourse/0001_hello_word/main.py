#coding: utf-8
#Importação da classe contendo informações do framework kivy
from kivy.app import App
from kivy.uix.label import Label
#Função que retorna valores
def build():
    #retornando o valor contido na classe de widget Label
    return Label(text='Hello Word!')
#Gerando uma instancia de kivy padrao 
#App().run()
#####################################
#Instancia de App Kivi Gerada 
hello_word = App()
#Associando a função a nossa instancia de App
hello_word.build = build
#Inicializando o metodo contido na instancia hello_word 
hello_word.run()


