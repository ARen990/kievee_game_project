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

    def jump(self, height):
        self.y = Window.height * 0 #jump smoot
        anim = Animation(y=self.y + height, duration=.3)
        anim += Animation(y=self.y, duration=.2)
        anim.start(self)


class MyApp(App):
    def build(self):
        Window.resizeable = False  # Prevent window resizing
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

        # Add jump buttons
        jump_button1 = Button(text="Jump", size_hint=(None, None), size=(100, 50), pos=(Window.width - 100, 30))
        layout.add_widget(jump_button1)
        #Sync jump button and function on_jump_button1_press
        jump_button1.bind(on_press=self.on_jump_button1_press)

        jump_button2 = Button(text="Jump X2", size_hint=(None, None), size=(100, 50), pos=(Window.width - 100, 85))
        layout.add_widget(jump_button2)
        #Sync jump button and function on_jump_button2_press
        jump_button2.bind(on_press=self.on_jump_button2_press)

        return layout
    
    def on_jump_button1_press(self, instance):
        self.stickman.jump(100)

    def on_jump_button2_press(self, instance):
        self.stickman.jump(200)

if __name__ == '__main__':
    Window.size = (800, 400)
    MyApp().run()