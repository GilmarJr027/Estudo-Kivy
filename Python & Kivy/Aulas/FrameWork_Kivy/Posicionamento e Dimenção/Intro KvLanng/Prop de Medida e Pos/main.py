from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):
    pass

class MedidaApp(App):

    def build(self):

        return RootWidget()

janela = MedidaApp()
from kivy.core.window import Window
Window.size = 450,450
janela.run()
