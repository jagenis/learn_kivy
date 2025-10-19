from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class DemoFloatLayout(App):
    def build(self):
        layout = FloatLayout()

        boton1 = Button(text="Esquina inferior izquierda",
                        size_hint=(0.3, 0.2),
                        pos_hint={"x": 0, "y": 0})

        boton2 = Button(text="Centro",
                        size_hint=(0.3, 0.2),
                        pos_hint={"center_x": 0.5, "center_y": 0.5})

        layout.add_widget(boton1)
        layout.add_widget(boton2)
        return layout

DemoFloatLayout().run()
