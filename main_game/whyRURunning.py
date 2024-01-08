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

        # Add the ground image
        self.ground = Image(source='image/orther/ground.png', allow_stretch=True, keep_ratio=False)
        self.ground.size_hint_x = None
        self.ground.width = Window.width
        self.ground.height = 48
        self.ground.pos_hint = {'center_x': .5, 'y': 50}
        layout.add_widget(self.ground)

        #add button jump
        button = Button(text="Jump", size_hint=(100, 40), size=(100, 50), pos=(Window.width / 2 - 50, 20))
        layout.add_widget(button)
        #Sync jump button and function on_jump_button_press
        button.bind(on_press=self.on_jump_button_press)

        return layout
    
    def on_jump_button_press(self, instance):
        self.stickman.jump()

if __name__ == '__main__':
    MyApp().run()