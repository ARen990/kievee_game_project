import random
import time
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color

def collides(rect1, rect2):
    r1x = rect1[0][0]
    r1y = rect1[0][1]
    r2x = rect2[0][0]
    r2y = rect2[0][1]
    r1w = rect1[1][0]
    r1h = rect1[1][1]
    r2w = rect2[1][0]
    r2h = rect2[1][1]

    if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
        return True
    else:
        return False

class Ground(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add the fading ground
        self.source ='image/orther/ground.png'
        self.allow_stretch = True 
        self.keep_ratio = False
        self.size_hint_x = None
        self.width = Window.width
        self.height = 48
        self.pos = (0, 50)

class Stickman(Image):
    def __init__(self, **kwargs):
        super(Stickman, self).__init__(**kwargs)
        self.source = 'image/stickman/stickrun1.png'
        self.allow_stretch = True
        self.size_hint = (None, None)
        self.size = (150, 150)
        self.pos = (0, 0)

        self.pressed_keys = set()
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        Clock.schedule_interval(self.move_step, 1/60.)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

    def jump(self, height):
        self.y = Window.height * 0 #jump smooth
        anim = Animation(y=self.y + height, duration=.3)
        anim += Animation(y=self.y, duration=.2)
        anim.start(self)

    def move_step(self, dt):
        cur_x = self.pos[0]
        cur_y = self.pos[1]
        # add random step
        step = random.uniform(10, 10000) * dt

        if 'w' in self.pressed_keys:
            cur_y += step
        if 's' in self.pressed_keys:
            cur_y -= step
        if 'a' in self.pressed_keys:
            cur_x -= step
        if 'd' in self.pressed_keys:
            cur_x += step
        self.pos = (cur_x, cur_y)

class Goal(Image):
    def __init__(self, **kwargs):
        super(Goal, self).__init__(**kwargs)
        self.source = 'image/floor_ob/dio.png'
        self.allow_stretch = True
        self.size_hint = (None, None)
        self.size = (100, 100)  # Adjust the size as needed

class ResetButton(Button):
    pass  # This is a placeholder for future customizations

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        
        # Add a white background
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color (RGBA)
            self.background_rect = Rectangle(size=(Window.width, Window.height), pos=self.pos)

        layout = Widget()

        # Add the stickman
        self.stickman = Stickman()
        layout.add_widget(self.stickman)

        self.ground = Ground()
        layout.add_widget(self.ground)

        # Create a random goal
        self.goal = Goal()
        self.place_goal_randomly()
        layout.add_widget(self.goal)

        # Add a timer label
        self.timer_label = Label(text='0:00', font_size='50sp', color=(0, 0, 0, 1), pos=(Window.width - 200, 600))
        layout.add_widget(self.timer_label)

        # Add a flag to track if the game is won
        self.game_won = False

        # Add reset button
        reset_button = ResetButton(text="Reset", size_hint=(None, None), size=(100, 50), pos=(Window.width - 100, 550))
        layout.add_widget(reset_button)
        reset_button.bind(on_press=self.reset_game)

        # add back button
        back_button = Button(text="<<Back", size_hint=(None, None), size=(100, 50), pos=(Window.width - 1000, 700))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        # add Append button
        append_button = Button(text="Have you encountered a problem?",font_size=25, size_hint=(None, None), size=(400, 50), pos=(Window.width / 2 +100, 700), color=(1, 0, 0, 1) )
        append_button.bind(on_press=self.switch_to_append)
        self.add_widget(append_button)

        # Add jump buttons
        jump_button1 = Button(text="Jump", size_hint=(None, None), size=(100, 50), pos=(Window.width - 100, 30))
        layout.add_widget(jump_button1)
        jump_button1.bind(on_press=self.on_jump_button1_press)

        jump_button2 = Button(text="Jump X2", size_hint=(None, None), size=(100, 50), pos=(Window.width - 100, 85))
        layout.add_widget(jump_button2)
        jump_button2.bind(on_press=self.on_jump_button2_press)

        self.add_widget(layout)

        # Initialize the timer
        self.start_time = time.time()
        self.elapsed_time = 0

        # Schedule the timer update method
        Clock.schedule_interval(self.timer_update, 1 / 60.)

    def timer_update(self, dt):
        if not self.game_won:  # Check if the game is not won
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)

            self.timer_label.text = '{:02d}:{:02d}'.format(minutes, seconds)
            self.elapsed_time = elapsed_time

            # Check for collision between stickman and goal
            stickman_rect = [(self.stickman.x, self.stickman.y), (self.stickman.width, self.stickman.height)]
            goal_rect = [(self.goal.x, self.goal.y), (self.goal.width, self.goal.height)]

            if collides(stickman_rect, goal_rect):
                self.game_won = True
                self.stop_timer()
                self.show_victory_popup()

    def stop_timer(self):
        Clock.unschedule(self.timer_update)

    def show_victory_popup(self):
        elapsed_time_formatted = self.format_elapsed_time()

        popup_content = BoxLayout(orientation='vertical', padding=10)
        popup_content.add_widget(Label(text=f'You won in {elapsed_time_formatted}!', font_size=20))
        
        # Add a button to return to the home page
        return_home_button = Button(text='Return to Home Page', size_hint=(None, None), size=(200, 50))
        return_home_button.bind(on_press=self.return_to_home)
        popup_content.add_widget(return_home_button)

        # Create the popup
        victory_popup = Popup(title='Congratulations!', content=popup_content, size_hint=(None, None), size=(400, 200))
        victory_popup.open()

    def return_to_home(self, instance):
        # Reset game state and return to the home page
        self.game_won = False
        self.start_time = time.time()
        self.stickman.pos = (0, 0)
        self.place_goal_randomly()

        # Close the victory popup
        App.get_running_app().root.current = 'start'

    def on_jump_button1_press(self, instance):
        self.stickman.jump(100)

    def on_jump_button2_press(self, instance):
        self.stickman.jump(200)

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'start'

    def switch_to_append(self, instance):
        app = app = App.get_running_app()
        app.root.current = 'append'

    def reset_game(self, instance):
        # Reset the game state here
        self.start_time = time.time()
        self.elapsed_time = 0
        self.stickman.pos = (0, 0)
        self.place_goal_randomly()

    def place_goal_randomly(self):
        goal_width = self.goal.width
        goal_height = self.goal.height
        window_width = Window.width
        window_height = Window.height

        random_x = random.randint(0, window_width - goal_width)
        random_y = random.randint(0, window_height - goal_height)

        self.goal.pos = (random_x, random_y)

    def format_elapsed_time(self):
        total_elapsed_time = self.elapsed_time + (time.time() - self.start_time)
        minutes = int(total_elapsed_time // 60)
        seconds = int(total_elapsed_time % 60)
        return '{:02d}:{:02d}'.format(minutes, seconds)

