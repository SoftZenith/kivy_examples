from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass

class SimpleKivy_3(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    SimpleKivy_3().run()
