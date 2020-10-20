from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from CP1404_Assignment_2.PlaceCollection import PlaceCollection


# TODO: Make sure to do the Project Reflection: (https://github.com/cp1404-students/travel-tracker-assignment-2-Leylun)
#   it is very important.

class Travel_Tracker(App):
    current_widgets = []

    def __init__(self, **kwargs):
        super(Travel_Tracker, self).__init__(**kwargs)
        self.root = Builder.load_file("Travel_Tracker_GUI.kv")
        self.title = "Travel_Tracker V2"
        self.collection = PlaceCollection()
        self.place_objects = self.collection.load_places()

    def build(self):
        self.make_widget()
        return self.root

    def make_widget(self):
        unvisited_places = 0
        for name in self.place_objects:
            if not name['visited']:
                unvisited_places += 1
            temp_but = Button(text=str(name), id=str(name))
            # temp_but.bind(on_press=lambda x: self.to_visited(name))
            temp_but.bind(on_press=lambda temp_but: self.toggle_visited(temp_but.text))
            self.root.ids.location_box.add_widget(temp_but)
            self.current_widgets.append(temp_but)
        self.root.ids.places_label.text = "Places to visit {}".format(unvisited_places)

    def switch_sort(self):
        # //Toggle switch for sort_types in switch_types
        switch_types = ["Visited", "Priority"]
        switch_val = switch_types.index(str(self.root.ids.switch_button.text)) + 1
        print(switch_val)
        switch_type = switch_types[switch_val] if switch_val < len(switch_types) \
            else switch_types[0]
        self.root.ids.switch_button.text = switch_type
        self.place_objects = self.collection.place_sort(switch_type)
        self.clear_widget()
        self.make_widget()

    def clear_inputs(self):
        # //Function to clear inputs, loop for ease of improvement
        root_ids = ['name_input', 'country_input', 'priority_input']
        for ids in root_ids:
            self.root.ids.ids.text = ""

    def add_place(self, name, country, priority):
        self.collection.add_place(name, country, priority)
        self.place_objects = self.collection.load_places()
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
                    self.root.ids.visited_label.text = "You visited {}".format(the_place.name)
                elif not the_place.visited:
                    self.root.ids.visited_label.text = "You need to visit {}".format(the_place.name)
            self.clear_widget()
        self.make_widget()


Travel_Tracker().run()
