from CP1404_Assignment_2.place import place
import csv


def save_places(current_places):
    # //Save given data into the csv file
    with open("places.csv", "w", newline="") as file_places:
        places = csv.writer(file_places)
        for location in current_places:
            places.writerow(location)
    return True


class PlaceCollection:
    list_places = []

    def __init__(self):
        # //Get data from csv file into class objects
        with open("places.csv", "r", newline="") as file_places:
            places = list(csv.reader(file_places))
        for location in places:
            if location[3] == "n":
                location[3] = False
            elif location[3] == "v":
                location[3] = True
            self.list_places.append(place(location[0], location[1], int(location[2]), bool(location[3])))

    def load_places(self):
        return self.list_places

    def place_sort(self):
        print()

    def add_place(self, name, country, priority):
        new_place = [name, country]
        for part in new_place:
            try:
                int(part)
            except TypeError:
                pass
            else:
                return False
            if part == "":
                return False
        try:
            int(priority)
        except TypeError:
            return False
        else:
            pass
        if priority < 1:
            return False
        return self.list_places.append(place(name, country, priority, False))
