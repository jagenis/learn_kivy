from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.metrics import dp


class Cell(RecycleDataViewBehavior, TextInput):
    def refresh_view_attrs(self, rv, index, data):
        self.row = data.get("row", 0)
        self.col = data.get("col", 0)
        self.table_ref = data.get("table_ref", None)
        self.readonly = data.get("readonly", False)
        self.text = data.get("text", "")
        self.multiline = False
        self.size_hint_y = None
        self.height = dp(40)
        return super().refresh_view_attrs(rv, index, data)

    def on_text_validate(self):
        if not self.readonly and self.table_ref:
            self.table_ref.update_cell(self.row, self.col, self.text)


class Table(RV := RecycleView):
    def __init__(self, headers, data, **kwargs):
        super().__init__(**kwargs)
        self.headers = headers
        self.data_matrix = data

        layout = RecycleGridLayout(
            cols=len(headers),
            default_size=(None, dp(40)),
            default_size_hint=(1, None),
            size_hint_y=None,
            spacing=2
        )
        layout.bind(minimum_height=layout.setter("height"))
        self.layout_manager = layout
        self.add_widget(layout)

        # Definir viewclass *después*
        self.viewclass = "Cell"

        self.refresh_table()

    def refresh_table(self):
        lst = []
        for c, h in enumerate(self.headers):
            lst.append({
                "text": f"[b]{h}[/b]",
                "markup": True,
                "readonly": True,
                "row": -1,
                "col": c,
                "table_ref": self
            })
        for i, row in enumerate(self.data_matrix):
            for j, val in enumerate(row):
                lst.append({
                    "text": str(val),
                    "readonly": False,
                    "row": i,
                    "col": j,
                    "table_ref": self
                })
        print("DEBUG: setting data of length", len(lst))
        self.data = lst

    def update_cell(self, r, c, v):
        print("Update:", r, c, v)
        self.data_matrix[r][c] = v


class MyApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical")
        root.add_widget(Label(text="Hola tabla", size_hint_y=None, height=30))
        t = Table(["A", "B", "C"],
              [[i * 3 + j + 1 for j in range(3)] for i in range(100)])
        root.add_widget(t)
        return root


if __name__ == "__main__":
    MyApp().run()
