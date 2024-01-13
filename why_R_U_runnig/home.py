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
        middle_image = Image(source='image/stickman/stickrun2.png', size_hint=(None, None), size=(250, 250),pos=(Window.width / 2 - 140, Window.height / 2 - 90))
        self.add_widget(middle_image)

        # add text name game
        about_text = Label(
            text="[color=FF9BD2]Why Are U Running[/color]",font_size=50, size_hint=(None, None),pos=(Window.width / 2 - 50, 200),markup=True)
        self.add_widget(about_text)

        # add start button
        start_button = Button(text="Start", size_hint=(None, None), size=(100, 50), pos=(Window.width / 2 - 50, 85))
        start_button.bind(on_press=self.start_game)
        self.add_widget(start_button)

        # add about button
        about_button = Button(text="About", size_hint=(None, None), size=(100, 50), pos=(Window.width / 2 - 50, 30))
        about_button.bind(on_press=self.switch_to_about)
        self.add_widget(about_button)

    def start_game(self, instance):
        app = App.get_running_app()
        app.root.current = 'game'  # Switch to the 'game' screen

    def switch_to_about(self, instance):
        app = App.get_running_app()
        app.root.current = 'about'

class About(Screen):
    def __init__(self, **kwargs):
        super(About, self).__init__(**kwargs)

        # add back button
        back_button = Button(text="<<Back", size_hint=(None, None), size=(100, 50), pos=(100, 400))
        back_button.bind(on_press=self.go_back)
        self.add_widget(back_button)

        # add text
        about_text = Label(
            text="[color=FF9BD2]Contact channels[/color]",font_size=50,pos=(0, 100),markup=True)
        self.add_widget(about_text)

        # add twitter button
        twitter_button = Button(text="Twitter", size_hint=(None, None), size=(100, 50), pos=(Window.width / 2 - 50, 200))
        twitter_button.bind(on_press=lambda x: self.open_link("https://x.com/Aenijin?s=20"))
        self.add_widget(twitter_button)

        # add Instagram button
        instagram_button = Button(text="Instagram", size_hint=(None, None), size=(100, 50), pos=(Window.width / 2 - 50, 150))
        instagram_button.bind(on_press=lambda x: self.open_link("https://www.instagram.com/dragon_sutdy?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="))
        self.add_widget(instagram_button)

        # add GitHub button
        github_button = Button(text="GitHub", size_hint=(None, None), size=(100, 50), pos=(Window.width / 2 - 50, 100))
        github_button.bind(on_press=lambda x: self.open_link("https://github.com/ARen990"))
        self.add_widget(github_button)

        # add youtube button
        youtube_button = Button(text="YouTube", size_hint=(None, None), size=(100, 50), pos=(Window.width / 2 - 50, 50))
        youtube_button.bind(on_press=lambda x: self.open_link("https://www.youtube.com/channel/UCHbOa_h7HDl3jTByZGTwKVw"))
        self.add_widget(youtube_button)

    def open_link(self, url):
        webbrowser.open(url)

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'start'

class MyApp(App):
    def build(self):
        # Create a ScreenManager
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(About(name='about'))
        return sm

if __name__ == '__main__':
    MyApp().run()
