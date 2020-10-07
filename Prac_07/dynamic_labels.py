from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynaWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_names = {"James", "Bob", "Connor", "Felix"}

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.make_widget()
        return self.root

    def make_widget(self):
        for name in self.label_names:
            temp_but = Label(text=name, id=name)
            temp_but.bind(on_release=self.enter_wid)
            self.root.ids.entries_box.add_widget(temp_but)

    def enter_wid(self, instance):
        name = instance.id
        self.status_text = "{}'s number is {}".format(name, self.label_names[name])


DynaWidgetsApp().run()
