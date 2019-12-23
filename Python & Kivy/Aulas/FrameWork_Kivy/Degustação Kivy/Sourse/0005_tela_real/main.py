from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def click():
    #envia para saida padrao o texto contido no TextInput txt_entrada_texto
    print(txt_entrada_texto.text)

def build():
    
    #Vincula a instancia  layout  a sua classe FloatLayout()
    layout = FloatLayout()
    #Defini a variavel sendo como global para poder ser acessada por outras funções
    global txt_entrada_texto

    #Cria o widget TextInput
    txt_entrada_texto = TextInput(text='SpaceDev')
    ##Cria o widget button
    btn_clique = Button(text='Clique Aqui')

    #adiciona o widget a instancia de layout
    layout.add_widget(txt_entrada_texto)
    #reinicializa as propriedades
    txt_entrada_texto.size_hint = None, None
    #define a altura
    txt_entrada_texto.height = 400
    #define a largura
    txt_entrada_texto.width = 300
    #posicionamento ao eixo x
    txt_entrada_texto.x = 150
    #posicionamento ao eixo y
    txt_entrada_texto.y = 150

    #adiciona o widget a instancia de layout
    layout.add_widget(btn_clique)
    #reinicializa as propriedades
    btn_clique.size_hint = None , None
    #define a altura
    btn_clique.height = 25
    #define a largura
    btn_clique.width = 120
    #posicionamento ao eixo x
    btn_clique.x = 220
    #posicionamento ao eixo y
    btn_clique.y = 80

    #Define o evento clique
    btn_clique.on_press = click

    #Retorna os dados da instancia de layout para função build
    return layout
#Cria a nossa instancia 
janela = App()
#defini o titulo do app
janela.title = ('App')
#vincula a função build a nossa instancia contida na classe App
janela.build = build
#Importa uma classe statica que manipula as dimenções da janela
from kivy.core.window import Window
#Define o tamanho da nossa janela
Window.size = 600,600
#inicializa nossa instancia
janela.run()