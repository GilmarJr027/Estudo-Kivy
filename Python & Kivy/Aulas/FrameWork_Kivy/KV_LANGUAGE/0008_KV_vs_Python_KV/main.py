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


    def __init__(self, **kwargs):
        super(TelaInicial, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt1 = Button(text="Tela 1")
        bt1.on_press = (self.on_press_bt)
        self.add_widget(bt1)
        self.add_widget(Button(text="bt clique 2"))
        self.add_widget(Button(text="bt clique 3"))


class TelaPos(BoxLayout):

    def on_press_bt2(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(TelaInicial())

    def __init__(self, **kwargs):
        super(TelaPos, self).__init__(**kwargs)
        self.orientation = "vertical"
        bt2 = Button(text="Tela 2")
        self.add_widget(bt2)
        bt2.on_press = (self.on_press_bt2) 



class KVvsPY(App):
    def build(self):
        return TelaInicial()
        
janela = KVvsPY()
janela.run()
    





