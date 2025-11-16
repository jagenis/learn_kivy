from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class DemoBoxLayout(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal", spacing=10, padding=10)
        layout.add_widget(Button(text="Botón 1", size_hint=(2, 1)))
        layout.add_widget(Button(text="Botón 2", size_hint=(0.25, 1)))
        layout.add_widget(Button(text="Botón 3", size_hint=(1, 1)))
        return layout

DemoBoxLayout().run()
