from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock

class ColorSizeWidget(BoxLayout):
    size_value = NumericProperty(14)                 # tamaño de fuente
    color_value = ListProperty([1, 0, 0, 1])         # color RGBA (rojo inicial)

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        
        self.boton = Button(text="Pulsa para cambiar",
                            font_size=self.size_value,
                            background_color=self.color_value)
        
        self.boton.bind(on_press=self.cambiar_apariencia)
        self.bind(size_value=self.actualizar_tamano)
        self.bind(color_value=self.actualizar_color)
        Clock.schedule_interval(self.cambiar_apariencia, 2)  # Cambia cada 2 segundos

        self.add_widget(self.boton)

    def cambiar_apariencia(self, *args):
        # cada vez que pulses, alterna tamaño y color
        if self.color_value == [1, 0, 0, 1]:  # rojo → verde
            self.color_value = [0, 0, 1, 1]
            self.size_value = 24
        else:  # verde → rojo
            self.color_value = [1, 0, 0, 1]
            self.size_value = 14

    def actualizar_tamano(self, instance, value):
        self.boton.font_size = value

    def actualizar_color(self, instance, value):
        self.boton.background_color = value


class PropVisualApp(App):
    def build(self):
        return ColorSizeWidget()


if __name__ == "__main__":
    PropVisualApp().run()
