from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

Window.size = (450, 615)

class Container(MDFloatLayout, FakeRectangularElevationBehavior):
    pass


class VehiScan(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("kv/welcome.kv"))
        screen_manager.add_widget(Builder.load_file("kv/mainpage.kv"))
        screen_manager.add_widget(Builder.load_file("kv/aboutus.kv"))
        return screen_manager 

if __name__ == "__main__":
    LabelBase.register(
        name="BPoppins", fn_regular="assets/fonts/Poppins-Bold.ttf")
    LabelBase.register(
        name="MPoppins", fn_regular="assets/fonts/Poppins-Medium.ttf")
    LabelBase.register(
        name="RPoppins", fn_regular="assets/fonts/Poppins-Regular.ttf")
    LabelBase.register(
        name="SBPoppins", fn_regular="assets/fonts/Poppins-SemiBold.ttf")
    VehiScan().run()