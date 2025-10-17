from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=10, padding=10)

        for i in range(1, 5):
            boton = Button(text=f"Botón {i}")
            layout.add_widget(boton)

        return layout

if __name__ == "__main__":
    GridApp().run()
