from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LayoutApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        etiqueta = Label(text="Pulsa el botón")
        boton = Button(text="Cambiar texto")

        boton.bind(on_press=lambda x: setattr(etiqueta, 'text', '¡Texto cambiado!'))
        layout.add_widget(etiqueta)
        layout.add_widget(boton)

        return layout

if __name__ == "__main__":
    LayoutApp().run()
