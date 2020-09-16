from Prac_06.guitar import Guitar

"""
Assumed we are not doing input checking or another other value checking.
"""


def main():
    guitars = []
    print_statements = ["Name: ", "Year: ", "Cost: "]
    num_of_guitars = 0
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    while True:
        values = []
        # With no checks for correct input, we can loop through all data.
        for statement in print_statements:
            user_input = input(statement)
            if not user_input:
                # Blank strings are considered false in boolean sense, thus simply.
                # Better to do it this was as well, considering if they make any entry blank it will end the loop.
                break
            values.append(user_input)
        if not user_input:
            # Added a second to break out of the while loop
            break
        guitars.append(Guitar(values[0], values[1], int(values[2])))
        # Final print statement before list is displayed.
        print(guitars[num_of_guitars])
        num_of_guitars += 1
    print("These are my guitars:")
    for index, guitar in enumerate(guitars, 1):
        # Ternary operator used with this, a bit too cramped for my liking however.
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {g.name} ({g.year}), worth $ {g.cost:,.2f} {}".format(index, vintage_string, g=guitar))


main()
