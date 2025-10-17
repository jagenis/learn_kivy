from kivy.app import App
from kivy.uix.button import Button

class BotonApp(App):
    def build(self):
        boton = Button(text="Haz clic aquí")
        boton.bind(on_press=self.mensaje)
        return boton

    def mensaje(self, instance):
        print("¡Has hecho clic!")

if __name__ == "__main__":
    BotonApp().run()
