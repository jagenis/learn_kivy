from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import PushMatrix, PopMatrix, Scale, Translate
from kivy.properties import NumericProperty


class FlipCard(Widget):
    flip_value = NumericProperty(1)

    def __init__(self, front, back, **kwargs):
        super().__init__(**kwargs)
        self.front_source = front
        self.back_source = back
        self.showing_front = True

        self.img = Image(source=self.front_source, allow_stretch=True, keep_ratio=False)
        self.add_widget(self.img)

        # Preparar transformaciones
        with self.canvas.before:
            PushMatrix()
            self.trans = Translate()
            self.scale = Scale(1, 1, 1)
        with self.canvas.after:
            PopMatrix()

        Clock.schedule_once(self.update_transform, 0)
        self.bind(flip_value=self.on_flip_value)

    def update_transform(self, *args):
        self.trans.x = self.center_x
        self.trans.y = self.center_y
        self.scale.origin = (self.center_x, self.center_y, 0)

    def on_flip_value(self, instance, value):
        # Escalado horizontal con espejo
        self.scale.x = value if value >= 0.001 else 0.001
        self.canvas.ask_update()  # 🔥 fuerza redibujo

    def flip(self):
        # Fase 1: reducir valor
        anim1 = Animation(flip_value=0.001, duration=0.25, t='out_quad')

        # Fase 2: restaurar valor
        anim2 = Animation(flip_value=1, duration=0.25, t='in_quad')

        def mid_flip(*args):
            # Cambiar imagen en el punto medio
            self.showing_front = not self.showing_front
            self.img.source = self.back_source if not self.showing_front else self.front_source

        anim1.bind(on_complete=lambda *a: (mid_flip(), anim2.start(self)))
        anim1.start(self)

    def on_touch_down(self, touch):
        # Voltea al hacer clic
        if self.collide_point(*touch.pos):
            self.flip()
            return True
        return super().on_touch_down(touch)

    def on_size(self, *args):
        self.update_transform()


class FlipApp(App):
    def build(self):
        layout = FloatLayout()

        card = FlipCard(
            front='cerdito.png',
            back='android.jpg',
            size_hint=(0.5, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(card)
        return layout


if __name__ == '__main__':
    FlipApp().run()
