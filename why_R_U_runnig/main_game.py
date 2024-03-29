from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from home import StartScreen, About, Append, Sound
from gamescreen import GameScreen

class MyApp(App):

    def build(self):
        sm = ScreenManager()
        start_screen = StartScreen(name='start')
        about_screen = About(name='about')
        game_screen = GameScreen(name='game')
        append_screen = Append(name='append')
        sound_screen = Sound(name='sound')
        
        sm.add_widget(start_screen)
        sm.add_widget(game_screen)
        sm.add_widget(about_screen)
        sm.add_widget(append_screen)
        sm.add_widget(sound_screen)

        return sm

if __name__ == '__main__':
    from kivy.core.window import Window
    Window.size = (800, 600)
    MyApp().run()