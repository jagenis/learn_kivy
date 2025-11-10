from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class DemoAnchorLayout(App):
    def build(self):
        anchor = AnchorLayout(anchor_x='left', anchor_y='top')
        anchor.add_widget(Button(text="Botón 1", size_hint=(0.3, 0.3), padding=(50, 50)))
        #anchor.add_widget(Button(text="Botón 2", size_hint=(0.4, 0.4), padding=(50, 50)))        
        return anchor
    
DemoAnchorLayout().run()