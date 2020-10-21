"""
CP1404 Travel_Tracker_2 Assignment 2 - Kivy Project to visually display locations
Tristan Harrington - tristan.harrington@my.jcu.edu.au
22/10/2020
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from CP1404_Assignment_2.PlaceCollection import PlaceCollection
from kivy.properties import ListProperty


class Travel_Tracker(App):
    current_widgets = []
    switch_types = ListProperty()

    def __init__(self, **kwargs):
        super(Travel_Tracker, self).__init__(**kwargs)
        self.root = Builder.load_file("Travel_Tracker_GUI.kv")
        self.title = "Travel_Tracker V2"
        self.switch_types = ["Visited", "Priority", "Country", "Name"]
        self.current_type = self.switch_types[0]
        self.first_run = True
        self.collection = PlaceCollection()
        self.place_objects = self.collection.load_places()

    def build(self):
        self.make_widget()
        return self.root

    def make_widget(self):
        unvisited_places = 0
        if self.first_run:
            self.switch_sort()
            self.first_run = False
        for name in self.place_objects:
            temp_but = Button(text=str(name), id=str(name))
            # temp_but.bind(on_press=lambda x: self.to_visited(name))
            temp_but.bind(on_press=lambda temp_but: self.toggle_visited(temp_but.text))
            if not name['visited']:
                unvisited_places += 1
                temp_but.background_color = 0.0, 1.0, 1.0, 1.0
            elif name['visited']:
                temp_but.background_color = 0.5, 0.5, 0.5, 1.0
            self.root.ids.location_box.add_widget(temp_but)
            self.current_widgets.append(temp_but)
        self.root.ids.places_label.text = "Places to visit {}".format(unvisited_places)

    def switch_sort(self):
        # //Toggle switch for sort_types in switch_types
        switch_val = self.switch_types.index(str(self.root.ids.switch_button.text))
        switch_type = self.switch_types[switch_val] if switch_val < len(self.switch_types) \
            else self.switch_types[0]
        # self.root.ids.switch_button.text = switch_type
        self.place_objects = self.collection.place_sort(str(switch_type))
        if not self.first_run:
            self.clear_widget()
            self.make_widget()

    def clear_inputs(self, clear_label):
        # //Function to clear inputs, loop for ease of improvement
        if clear_label:
            self.root.ids.visited_label.text = ""
        root_ids = [self.root.ids.name_input, self.root.ids.country_input,
                    self.root.ids.priority_input]
        for root in root_ids:
            root.text = ""

    def add_place(self, name, country, priority):
        self.root.ids.visited_label.text = self.collection.add_place(name, country, priority)
        self.place_objects = self.collection.load_places()
        self.clear_inputs(False)
        self.clear_widget()
        self.make_widget()

    def clear_widget(self):
        # method to clear widgets, resets current widgets to prevent computation lag at higher numbers
        for widget in self.current_widgets:
            self.root.ids.location_box.remove_widget(widget)
        self.current_widgets = []

    def toggle_visited(self, given_name):
        # method to turn place objects visited or unvisited
        for the_place in self.place_objects:
            if given_name == str(the_place):
                the_place.tog_visited()
                if the_place.visited:
                    if the_place.important:
                        self.root.ids.visited_label.text = "You visited {}. Great Travelling!".format(the_place.name)
                    else:
                        self.root.ids.visited_label.text = "You visited {}".format(the_place.name)
                elif not the_place.visited:
                    if the_place.important:
                        self.root.ids.visited_label.text = "You need to visit {}. Get going!".format(the_place.name)
                    else:
                        self.root.ids.visited_label.text = "You need to visit {}".format(the_place.name)
            self.clear_widget()
        self.make_widget()
    
    def on_stop(self):
        self.collection.save_places(self.place_objects)


Travel_Tracker().run()

