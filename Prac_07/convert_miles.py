from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from tkinter import *


class ConvertMiles(App):
    def build(self):
        root = Tk()
        Window.size = (root.winfo_screenwidth()/3, root.winfo_screenheight()/4)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles.kv')
        return self.root

    def to_kilometers(self, value):
        try:
            int(value)
        except TypeError:
            self.root.ids.Converted_Value.text = str(0.0)
        except ValueError:
            self.root.ids.Converted_Value.text = str(0.0)
        else:
            result = int(value) * 1.609
            self.root.ids.Converted_Value.text = str(result)

    def value_change(self, value, up):
        try:
            int(value)
        except TypeError:
            value = 0
        except ValueError:
            value = 0
        result = int(value) + up
        self.root.ids.number_input.text = str(result)
        self.to_kilometers(str(result))


ConvertMiles().run()
