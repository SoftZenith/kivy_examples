from kivy.app import App
#kivy.require("1.9.2")
from kivy.uix.floatlayout import FloatLayout

class SimpleKivy_4(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    SimpleKivy_4().run()
