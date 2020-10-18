from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty
import csv
from CP1404_Assignment_2.place import place


# TODO: Make sure to do the Project Reflection: (https://github.com/cp1404-students/travel-tracker-assignment-2-Leylun)
#   it is very important.

class DynaWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # //Get data from csv file into class objects
        with open("places.csv", "r", newline="") as file_places:
            list_places = list(csv.reader(file_places))
        print(list_places)
        self.place_objects = []
        for location in list_places:
            if location[3] == "n":
                location[3] = True
            elif location[3] == "":
                location[3] = False
            self.place_objects.append(place(location[0], location[1], int(location[2]), bool(location[3])))
        # for thing in place_objects:
        #     print(thing)

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file("Travel_Tracker_GUI.kv")
        self.make_widget()
        return self.root

    def make_widget(self):
        for name in self.place_objects:
            temp_lab = Label(text=str(name), id=str(name))
            # temp_lab.bind(on_release=self.enter_wid)
            self.root.ids.location_box.add_widget(temp_lab)

    # def enter_wid(self, instance):
    #     name = instance.id
    #     self.status_text = "{}'s number is {}".format(name, self.place_objects[name])

    def switch_sort(self):
        # Toggle switch for sort_types in switch_types
        switch_types = ["Visited", "Priority"]
        switch_val = switch_types.index(str(self.root.ids.switch_button.text)) + 1
        print(switch_val)
        self.root.ids.switch_button.text = switch_types[switch_val] if switch_val < len(switch_types) \
            else switch_types[0]


DynaWidgetsApp().run()
