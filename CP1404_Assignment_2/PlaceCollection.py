from CP1404_Assignment_2.place import place
import csv


class PlaceCollection:
    list_places = []

    def __init__(self):
        # //Get data from csv file into class objects
        with open("places.csv", "r", newline="") as file_places:
            places = list(csv.reader(file_places))
        for location in places:
            if location[3] == "n":
                location[3] = True
            elif location[3] == "v":
                location[3] = False
            self.list_places.append(place(location[0], location[1], int(location[2]), bool(location[3])))

    def load_places(self):
        return self.list_places

    def place_sort(self):
        print()

    def add_place(self):
        print()

    def save_places(self):
        print()
