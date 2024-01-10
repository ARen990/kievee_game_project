from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from home import StartScreen
from gamescreen import GameScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        start_screen = StartScreen(name='start')
        game_screen = GameScreen(name='game')

        sm.add_widget(start_screen)
        sm.add_widget(game_screen)

        return sm

if __name__ == '__main__':
    from kivy.core.window import Window
    Window.size = (800, 400)
    MyApp().run()