from CP1404_Assignment_2.PlaceCollection import PlaceCollection


def main():
    collection = PlaceCollection()
    list_of_places = collection.load_places()
    for location in list_of_places:
        print(location)
    sort_types = ['visited', 'priority', 'country', 'name']
    for sort in sort_types:
        list_of_places = collection.place_sort(sort)
        for location in list_of_places:
            print("Sort_type: {} | List_Places: {}".format(sort, location))
    data_values = [input("Name:"), input("Country:"), input("Priority")]
    print(collection.add_place(data_values[0], data_values[1], data_values[2]))
    # list_of_places = collection.load_places()
    # collection.save_places(list_of_places)


main()

