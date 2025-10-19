from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.metrics import dp


class EditableTable(GridLayout):
    """Tabla editable con varias columnas"""

    def __init__(self, headers, data, **kwargs):
        super().__init__(**kwargs)
        self.cols = len(headers)
        self.size_hint_y = None
        self.spacing = 2
        self.padding = 2
        self.bind(minimum_height=self.setter('height'))

        self.headers = headers
        self.data_matrix = data

        # Encabezados
        for h in headers:
            lbl = Label(
                text=f"[b]{h}[/b]",
                markup=True,
                size_hint_y=None,
                height=dp(30),
                bold=True,
                color=(1, 1, 1, 1)
            )
            self.add_widget(lbl)

        # Filas de datos
        self.load_data()

    def load_data(self):
        """Crea las filas y celdas editables"""
        for i, row in enumerate(self.data_matrix):
            for j, value in enumerate(row):
                ti = TextInput(
                    text=str(value),
                    multiline=False,
                    size_hint_y=None,
                    height=dp(30),
                )
                # Evento cuando el usuario termina de escribir
                ti.bind(on_text_validate=lambda instance, r=i, c=j: self.update_cell(r, c, instance.text))
                self.add_widget(ti)

    def update_cell(self, row, col, value):
        """Actualizar los datos internos"""
        self.data_matrix[row][col] = value
        print(f"Actualizado: fila {row}, columna {col} = {value}")


class TableApp(App):
    def build(self):
        headers = ["Nombre", "Edad", "Ciudad"]
        data = [
            ["Ana", "25", "Madrid"],
            ["Luis", "30", "Barcelona"],
            ["María", "22", "Valencia"],
            ["Carlos", "28", "Sevilla"],
            ["Lucía", "35", "Bilbao"],
            ["Jorge", "41", "Granada"]
        ]

        root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        title = Label(
            text="[b]Tabla editable en Kivy[/b]",
            markup=True,
            size_hint_y=None,
            height=40
        )
        root.add_widget(title)

        scroll = ScrollView(size_hint=(1, 1))
        table = EditableTable(headers, data)
        scroll.add_widget(table)
        root.add_widget(scroll)

        return root


if __name__ == "__main__":
    TableApp().run()
