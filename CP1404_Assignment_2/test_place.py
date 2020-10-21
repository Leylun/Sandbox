from CP1404_Assignment_2.place import place


def main():
    test_place = place("Uluru", "Australia", 2, False)
    print(test_place.important)
    print(test_place)
    print("Current Priority: {}".format(test_place.visited))
    test_place.tog_visited()
    print("New Priority: {}".format(test_place.visited))


main()
