from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label  # اضافه کردن ایمپورت لازم

my_kv = Builder.load_string(
'''
Label:
    text: "[b] Hello [color=#12dc30]world[/color][/b]"
    markup: True
'''
)

class HelloWorld(App):
    def build(self):
        return my_kv

HelloWorld().run()
