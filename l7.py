from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock


# --- MODELO / VISTA (solo interfaz y propiedades) ---
class ColorSizeWidget(BoxLayout):
    size_value = NumericProperty(14)
    color_value = ListProperty([1, 0, 0, 1])  # rojo

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.boton = Button(
            text="Pulsa para cambiar",
            font_size=self.size_value,
            background_color=self.color_value
        )
        self.add_widget(self.boton)

        # sincroniza propiedades con el botón
        self.bind(size_value=self._actualizar_tamano)
        self.bind(color_value=self._actualizar_color)

    def _actualizar_tamano(self, instance, value):
        self.boton.font_size = value

    def _actualizar_color(self, instance, value):
        self.boton.background_color = value


# --- CONTROLADOR (gestiona la lógica, usa el modelo/vista) ---
class ColorController:
    def __init__(self, view: ColorSizeWidget):
        self.view = view
        # eventos
        self.view.boton.bind(on_press=self.cambiar_apariencia)
        # temporizador
        Clock.schedule_interval(self.cambiar_apariencia, 2)

    def cambiar_apariencia(self, *args):
        """Alterna color y tamaño"""
        if self.view.color_value == [1, 0, 0, 1]:  # rojo → azul
            self.view.color_value = [0, 0, 1, 1]
            self.view.size_value = 24
        else:  # azul → rojo
            self.view.color_value = [1, 0, 0, 1]
            self.view.size_value = 14


# --- APLICACIÓN ---
class PropVisualApp(App):
    def build(self):
        widget = ColorSizeWidget()
        self.controller = ColorController(widget)
        return widget


if __name__ == "__main__":
    PropVisualApp().run()
