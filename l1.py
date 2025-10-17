from kivy.app import App
from kivy.uix.label import Label

class MiPrimeraApp(App):
    def build(self):
        return Label(text="¡Hola mundo Kivy!")

if __name__ == "__main__":
    MiPrimeraApp().run()
