from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.lang import Builder

class Stickman(Image):
    def __init__(self, **kwargs):
        super(Stickman, self).__init__(**kwargs)
        self.source = 'image/stickman/stickrun1.png'
        self.allow_stretch = True
        self.size_hint = (None, None)
        self.size = (100, 100)
        self.pos_hint = {'center_x': .5, 'center_y': .1}

    def jump(self):
        anim = Animation(y=self.y+100, duration=.3)
        anim += Animation(y=self.y, duration=.2)
        anim.start(self)

class MyApp(App):
    def build(self):
        layout = Widget()
        self.stickman = Stickman()
        layout.add_widget(self.stickman)
        return layout

if __name__ == '__main__':
    MyApp().run()