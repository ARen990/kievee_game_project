from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader
import webbrowser

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)


        setmusic_button = Button(text="setting", font_size=25, size_hint=(None, None),size=(150, 50), pos=(Window.width / 2 - 500 , 700))
        setmusic_button.bind(on_press=self.switch_to_sound)
        self.add_widget(setmusic_button)

        # add image
        middle_image = Image(source='image/stickman/stickrun2.png', size_hint=(None, None), size=(300, 300),pos=(Window.width / 2 - 140, Window.height / 2))
        self.add_widget(middle_image)

        # add Append button
        append_button = Button(text="Have you encountered a problem?", font_size=25, size_hint=(None, None),size=(400, 50), pos=(Window.width / 2 + 100, 700), color=(1, 0, 0, 1))
        append_button.bind(on_press=self.switch_to_append)
        self.add_widget(append_button)

        # add text name game
        name_text = Label(
            text="[color=FF9BD2]Why Are U Running[/color]", font_size=100, size_hint=(None, None),
            pos=(Window.width / 2 - 50, 300), markup=True)
        self.add_widget(name_text)

        # add start button
        start_button = Button(text="Start", font_size=50, size_hint=(None, None), size=(150, 100),pos=(Window.width / 2 - 50, 150))
        start_button.bind(on_press=self.start_game)
        self.add_widget(start_button)

        # add about button
        about_button = Button(text="About", font_size=50, size_hint=(None, None), size=(150, 100),pos=(Window.width / 2 - 50, 30))
        about_button.bind(on_press=self.switch_to_about)
        self.add_widget(about_button)

    # change volume
    def on_volume_change(self, instance, value):
        if self.background_music:
            self.background_music.volume = value

    def set_volume(self, volume):
        if self.background_music:
            self.background_music.volume = volume
            self.volume_slider.value = volume

    def start_game(self, instance):
        app = App.get_running_app()
        app.root.current = 'game'  # Switch to the 'game' screen

    def switch_to_about(self, instance):
        app = App.get_running_app()
        app.root.current = 'about'

    def switch_to_append(self, instance):
        app = app = App.get_running_app()
        app.root.current = 'append'

    def switch_to_sound(self, instance):
        app = app = App.get_running_app()
        app.root.current = 'sound'


class About(Screen):
    def __init__(self, **kwargs):
        super(About, self).__init__(**kwargs)

        # Load sound effect
        self.sound_effect = SoundLoader.load('image/music/chinese_music.mp3')

        # add image
        me_image = Image(source='image/stickman/stickmob4.png', size_hint=(None, None), size=(350, 350),pos=(Window.width / 2 - 450, Window.height / 2 - 250))
        self.add_widget(me_image)

        # add back button
        back_button = Button(text="<<Back", font_size=40, size_hint=(None, None), size=(150, 100),pos=(Window.width - 1000, 650))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        # add start button
        start_button = Button(text="Start", font_size=50, size_hint=(None, None), size=(150, 100),pos=(Window.width - 1000, 0))
        start_button.bind(on_press=self.start_game)
        self.add_widget(start_button)

        # add text
        about_text = Label(
            text="[color=FF9BD2]Contact channels[/color]", font_size=100, pos=(0, 200), markup=True)
        self.add_widget(about_text)

        # add twitter button
        twitter_button = Button(text="Twitter", font_size=50, size_hint=(None, None), size=(300, 100),
                                pos=(Window.width / 2 - 50, 350))
        twitter_button.bind(on_press=lambda x: self.open_link("https://x.com/Aenijin?s=20"))
        self.add_widget(twitter_button)

        # add Instagram button
        instagram_button = Button(text="Instagram", font_size=50, size_hint=(None, None), size=(300, 100),pos=(Window.width / 2 - 50, 250))
        instagram_button.bind(on_press=lambda x: self.open_link(
            "https://www.instagram.com/dragon_sutdy?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="))
        self.add_widget(instagram_button)

        # add GitHub button
        github_button = Button(text="GitHub", font_size=50, size_hint=(None, None), size=(300, 100),pos=(Window.width / 2 - 50, 150))
        github_button.bind(on_press=lambda x: self.open_link("https://github.com/ARen990"))
        self.add_widget(github_button)

        # add youtube button
        youtube_button = Button(text="YouTube", font_size=50, size_hint=(None, None), size=(300, 100),
                                pos=(Window.width / 2 - 50, 50))
        youtube_button.bind(on_press=lambda x: self.open_link("https://www.youtube.com/channel/UCHbOa_h7HDl3jTByZGTwKVw"))
        self.add_widget(youtube_button)

    def open_link(self, url):
        webbrowser.open(url)

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'start'

    def start_game(self, instance):
        app = App.get_running_app()
        app.root.current = 'game'

class Append(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        # Load sound effect
        self.sound_effect = SoundLoader.load('image/music/chinese_music.mp3')

        # add back button
        back_button = Button(text="<<Back", font_size=40, size_hint=(None, None), size=(150, 100),pos=(Window.width - 1000, 650))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        # add start button
        start_button = Button(text="Start", font_size=50, size_hint=(None, None), size=(150, 100),pos=(Window.width - 150, 650))
        start_button.bind(on_press=self.start_game)
        self.add_widget(start_button)

        append_text = Label(
            text="[color=FF9BD2]1.If you encounter any problems \n please close and restart the game. \n 2.If you start the game and win, follow step 1.[/color]",
            font_size=40, pos=(0, 150), markup=True)
        self.add_widget(append_text)

        add1_text = Label(
            text="[color=#FFFFFF]KRITTIMON[/color]", font_size=30, pos=(Window.width - 700, Window.width / 2 - 600),
            markup=True)
        self.add_widget(add1_text)

        add2_text = Label(
            text="[color=#FFFFFF]I apologize for the inconvenience.[/color]", font_size=30,
            pos=(Window.width - 800, Window.width / 2 - 650), markup=True)
        self.add_widget(add2_text)

        # add image
        me_image = Image(source='image/stickman/stickdead.png', size_hint=(None, None), size=(300, 300),pos=(Window.width / 2 - 400, Window.height / 2 - 300))
        self.add_widget(me_image)

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'start'

    def start_game(self, instance):
        app = App.get_running_app()
        app.root.current = 'game'
        if self.sound_effect:
            self.sound_effect.play()
    
class Sound(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        # Load background music
        self.background_music = SoundLoader.load('image/music/chinese_music.mp3')
        if self.background_music:
            self.background_music.loop = True
            self.background_music.play()

        # Volume slider
        self.volume_slider = Slider(min=0, max=1, value=1, step=0.01, size_hint=(None, None), width=300, height=50,
                                    pos=(Window.width / 2 - 150, 600))
        self.volume_slider.bind(value=self.on_volume_change)
        self.add_widget(self.volume_slider)

        # Volume control buttons
        volume_buttons = [
            {"text": "10%", "volume": 0.1},
            {"text": "25%", "volume": 0.25},
            {"text": "50%", "volume": 0.5},
            {"text": "75%", "volume": 0.75},
            {"text": "100%", "volume": 1.0}
        ]

        for button_info in volume_buttons:
            volume_button = Button(text=button_info["text"], font_size=20, size_hint=(None, None), size=(100, 50),
                                   pos=(Window.width / 2 - 50, 500 - volume_buttons.index(button_info) * 70))
            volume_button.bind(on_press=lambda x, vol=button_info["volume"]: self.set_volume(vol))
            self.add_widget(volume_button)

        # add back button
        back_button = Button(text="<<Back", font_size=40, size_hint=(None, None), size=(150, 100),pos=(Window.width - 1000, 650))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

    # Add the missing on_volume_change method
    def on_volume_change(self, instance, value):
        if self.background_music:
            self.background_music.volume = value

    def set_volume(self, volume):
        if self.background_music:
            self.background_music.volume = volume
            self.volume_slider.value = volume
    
    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'start'
