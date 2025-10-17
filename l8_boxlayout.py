from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class DemoBoxLayout(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal", spacing=10, padding=10)
        layout.add_widget(Button(text="Botón 1"))
        layout.add_widget(Button(text="Botón 2"))
        layout.add_widget(Button(text="Botón 3"))
        return layout

DemoBoxLayout().run()
