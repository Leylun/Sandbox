from Prac_06.guitar import Guitar


def main():
    new_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013)
    print("{} get_age() - Expected 98. Got {}".format(new_guitar.name, new_guitar.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is_vintage - Expected True. Got {}".format(new_guitar.name, new_guitar.is_vintage()))
    print("{} is_vintage - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))
    # Could have created it to do the functions of the class here to prove, but if the class functions where written
    # wrong it would make sense to assume functions here are written wrong, or perhaps they are both incorrect.


main()
