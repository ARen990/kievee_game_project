from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.graphics import Rectangle

class Ground(Image):
    pass

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

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        layout = Widget()

        # Add the stickman
        self.stickman = Stickman()
        layout.add_widget(self.stickman)

        # Add the fading ground
        self.ground = Image(source='image/orther/ground.png', allow_stretch=True, keep_ratio=False)
        self.ground.size_hint_x = None
        self.ground.width = Window.width
        self.ground.height = 48
        self.ground.pos_hint = {'center_x': .5, 'y': 50}
        layout.add_widget(self.ground)

        # add back button
        back_button = Button(text="<<Back", size_hint=(None, None), size=(100, 50), pos=(100, 400))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        # Add jump buttons
        jump_button1 = Button(text="Jump", size_hint=(None, None), size=(100, 50), pos=(Window.width - 100, 30))
        layout.add_widget(jump_button1)
        jump_button1.bind(on_press=self.on_jump_button1_press)

        jump_button2 = Button(text="Jump X2", size_hint=(None, None), size=(100, 50), pos=(Window.width - 100, 85))
        layout.add_widget(jump_button2)
        jump_button2.bind(on_press=self.on_jump_button2_press)

        self.add_widget(layout)

    def on_jump_button1_press(self, instance):
        self.stickman.jump(100)

    def on_jump_button2_press(self, instance):
        self.stickman.jump(200)

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'start'
    
