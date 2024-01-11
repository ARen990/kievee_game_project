from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

        #add image
        middle_image = Image(source='image/stickman/stickrun2.png', size_hint=(None, None), size=(250, 250),pos=(Window.width / 2 - 140, Window.height / 2 - 90))
        self.add_widget(middle_image)

        #add start button
        about_button = Button(text="About", size_hint=(None, None), size=(100, 50), pos=(Window.width / 2 - 50, 85))
        about_button.bind(on_press=self.show_about)
        self.add_widget(about_button)

        #add about button
        start_button = Button(text="About", size_hint=(None, None), size=(100, 50), pos=(Window.width / 2 - 50, 30))
        start_button.bind(on_press=self.start_game)
        self.add_widget(start_button)


    def start_game(self, instance):
        app = App.get_running_app()
        app.root.current = 'game'  # Switch to the 'game' screen

    def show_about(self, instance):
        print("About button pressed - implement your logic here")

if __name__ == '__main__':
    class MyApp(App):
        def build(self):
            return StartScreen()
