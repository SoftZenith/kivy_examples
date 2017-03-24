from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
import mechanize

class ContainerBox(GridLayout):
    def callback(self):
        self.ids.etiqueta.text = "Presionado"
        print self.ids.destino.text
        print self.ids.origen.text

class SimpleKivy_5(App):
    def build(self):
        return ContainerBox()

    def imprimir(self):
        pass

if __name__ == "__main__":
    SimpleKivy_5().run()
