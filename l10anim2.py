from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import PushMatrix, PopMatrix, Rotate, Color, Rectangle
from kivy.properties import NumericProperty, BooleanProperty
from kivy.core.window import Window


class FlipCard(FloatLayout):
    angle = NumericProperty(0)
    showing_front = BooleanProperty(True)

    def __init__(self, front, back, **kwargs):
        super().__init__(**kwargs)
        self.front_source = front
        self.back_source = back
        self.flipping = False

        # === IMAGEN (se actualiza dinámicamente) ===
        self.img = Image(
            source=self.front_source,
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        self.add_widget(self.img)

        # === FONDO BLANCO (opcional, para evitar transparencias) ===
        with self.canvas.before:
            self.bg_color = Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

        # === TRANSFORMACIÓN 3D ===
        with self.canvas.before:
            PushMatrix()
            self.rotate = Rotate(angle=0, axis=(0, 1, 0))
            # Origen en el centro del widget
            self.rotate.origin = (self.width / 2, self.height / 2)

        with self.canvas.after:
            PopMatrix()

        # === BINDINGS ===
        self.bind(pos=self.update_graphics)
        self.bind(size=self.update_graphics)
        self.bind(angle=self.update_angle)
        Clock.schedule_once(self.update_graphics, 0)

    def update_graphics(self, *args):
        # Actualizar fondo
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

        # Actualizar origen de rotación (centro exacto)
        self.rotate.origin = (self.center_x, self.center_y)

        # Asegurar que la imagen ocupe todo
        self.img.size = self.size
        self.img.pos = self.pos

    def update_angle(self, instance, value):
        self.rotate.angle = value

        # === EFECTO DE SOMBRA AL GIRAR ===
        norm_angle = abs((value % 180) - 90)
        darkness = 1 - (norm_angle / 90) * 0.4  # de 0.6 a 1.0
        self.img.opacity = darkness
        self.bg_color.a = darkness

    def flip(self):
        if self.flipping:
            return
        self.flipping = True

        # Dirección según la cara actual
        target = 180 if self.showing_front else -180

        anim = Animation(angle=target, duration=0.6, t='out_quad')

        def on_progress(animation, widget, progress):
            angle = self.angle % 360
            # Cambiar cara cuando está de espaldas
            if 80 <= angle <= 100 and self.showing_front:
                self.showing_front = False
                self.img.source = self.back_source
                self.img.reload()  # Forzar recarga
            elif 260 <= angle <= 280 and not self.showing_front:
                self.showing_front = True
                self.img.source = self.front_source
                self.img.reload()
                self.angle = 0
                animation.stop(self)
                self.flipping = False

        def on_complete(*args):
            self.angle = 0
            self.showing_front = True
            self.img.source = self.front_source
            self.img.reload()
            self.flipping = False

        anim.bind(on_progress=on_progress, on_complete=on_complete)
        anim.start(self)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.flip()
            return True
        return super().on_touch_down(touch)


class FlipApp(App):
    def build(self):
        Window.clearcolor = (0.15, 0.15, 0.15, 1)

        layout = FloatLayout()

        card = FlipCard(
            front='cerdito.png',
            back='android.jpg',
            size_hint=(0.5, 0.7),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(card)
        return layout


if __name__ == '__main__':
    FlipApp().run()