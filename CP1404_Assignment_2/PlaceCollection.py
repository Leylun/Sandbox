from CP1404_Assignment_2.place import place
import csv


def save_places(current_places):
    # //Save given data into the csv file
    with open("places.csv", "w", newline="") as file_places:
        places = csv.writer(file_places)
        for location in current_places:
            places.writerow(location)
    return True


def sorting_algorithm(sorting_list, sorting_type):
    sorted_list = []
    for the_place in sorting_list:
        sorted_list.append(the_place[sorting_type])
    sorted_list.sort()
    list_index = 0
    for value in sorted_list:
        for the_place in sorting_list:
            if value == the_place[sorting_type]:
                sorted_list[list_index] = sorting_list[sorting_list.index(the_place)]
                list_index += 1
    return sorted_list


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

    def place_sort(self, given_order):
        # // Switch order based on function argument
        if given_order == "Priority":
            self.list_places = sorting_algorithm(self.list_places, 'priority')
            return self.list_places
        elif given_order == "Visited":
            visited_list = []
            unvisited_list = []
            for places in self.list_places:
                if places['visited']:
                    visited_list.append(places)
            visited_list = sorting_algorithm(visited_list, 'priority')
            for places in self.list_places:
                if not places['visited']:
                    unvisited_list.append(places)
            unvisited_list = sorting_algorithm(unvisited_list, 'priority')
            self.list_places = visited_list + unvisited_list
        elif given_order == "Country":
            self.list_places = sorting_algorithm(self.list_places, 'country')
            return self.list_places
        elif given_order == "Name":
            self.list_places = sorting_algorithm(self.list_places, 'name')
            return self.list_places
        return self.list_places

    def add_place(self, name, country, priority):
        new_place = [name, country]
        for part in new_place:
            try:
                int(part)
            except ValueError:
                pass
            else:
                return "All fields must be completed"
            if part == "":
                return "All fields must be completed"
        if priority == "":
            return "All fields must be completed"
        try:
            int(priority)
        except ValueError:
            return "Please enter a valid number"
        else:
            priority = int(priority)
            if priority < 1:
                return "Priority must be > 0"
            self.list_places.append(place(name, country, priority, False))
            return str(self.list_places[-1]) + " added"
