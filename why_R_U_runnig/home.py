from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
import webbrowser

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        # add image
        middle_image = Image(source='image/stickman/stickrun2.png', size_hint=(None, None), size=(300, 300),pos=(Window.width / 2 - 140, Window.height / 2 ))
        self.add_widget(middle_image)

        # add Append button
        append_button = Button(text="Have you encountered a problem?",font_size=25, size_hint=(None, None), size=(400, 50), pos=(Window.width / 2 +100, 700), color=(1, 0, 0, 1) )
        self.add_widget(append_button)

        # add text name game
        name_text = Label(
            text="[color=FF9BD2]Why Are U Running[/color]",font_size=100, size_hint=(None, None),pos=(Window.width / 2 - 50, 300),markup=True)
        self.add_widget(name_text)

        # add start button
        start_button = Button(text="Start",font_size=50, size_hint=(None, None), size=(150, 100), pos=(Window.width / 2 - 50, 150))
        start_button.bind(on_press=self.start_game)
        self.add_widget(start_button)

        # add about button
        about_button = Button(text="About", font_size=50,  size_hint=(None, None), size=(150, 100), pos=(Window.width / 2 - 50, 30))
        about_button.bind(on_press=self.switch_to_about)
        self.add_widget(about_button)

    def start_game(self, instance):
        app = App.get_running_app()
        app.root.current = 'game'  # Switch to the 'game' screen

    def switch_to_about(self, instance):
        app = App.get_running_app()
        app.root.current = 'about'

    def switch_to_append(self, instance):
        app = app = App.get_running_app()
        app.root.current = 'append'

class About(Screen):
    def __init__(self, **kwargs):
        super(About, self).__init__(**kwargs)

        # add back button
        back_button = Button(text="<<Back",  font_size=40, size_hint=(None, None), size=(150, 100), pos=(Window.width - 1000, 650))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        # add text
        about_text = Label(
            text="[color=FF9BD2]Contact channels[/color]",font_size=100,pos=(0, 200),markup=True)
        self.add_widget(about_text)

        # add twitter button
        twitter_button = Button(text="Twitter", font_size=50, size_hint=(None, None), size=(300, 100), pos=(Window.width / 2 - 50, 350))
        twitter_button.bind(on_press=lambda x: self.open_link("https://x.com/Aenijin?s=20"))
        self.add_widget(twitter_button)

        # add Instagram button
        instagram_button = Button(text="Instagram", font_size=50, size_hint=(None, None), size=(300, 100), pos=(Window.width / 2 - 50, 250))
        instagram_button.bind(on_press=lambda x: self.open_link("https://www.instagram.com/dragon_sutdy?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="))
        self.add_widget(instagram_button)

        # add GitHub button
        github_button = Button(text="GitHub", font_size=50, size_hint=(None, None), size=(300, 100), pos=(Window.width / 2 - 50, 150))
        github_button.bind(on_press=lambda x: self.open_link("https://github.com/ARen990"))
        self.add_widget(github_button)

        # add youtube button
        youtube_button = Button(text="YouTube", font_size=50, size_hint=(None, None), size=(300, 100), pos=(Window.width / 2 - 50, 50))
        youtube_button.bind(on_press=lambda x: self.open_link("https://www.youtube.com/channel/UCHbOa_h7HDl3jTByZGTwKVw"))
        self.add_widget(youtube_button)

    def open_link(self, url):
        webbrowser.open(url)

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'start'

class Append(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)