def main():
    check_loop = True
    while check_loop:
        user_input = input("Please input [C]elsius or [F]ahrenheit (Use C or F to type answer)").upper()
        if user_input == "C":
            given_temperature = int(input("Please input Celsius Temperature."))
            print("Fahrenheit Temperature:", switch_temperature(given_temperature, 0))
            check_loop = False
        elif user_input == "F":
            given_temperature = int(input("Please input Fahrenheit Temperature."))
            print("Celsius Temperature:", switch_temperature(0, given_temperature))
            check_loop = False
        else:
            pass


def switch_temperature(celsius, fahrenheit):
    new_temperature = 0
    if celsius > 0:
        new_temperature = (celsius * 9 / 5) + 32
    elif fahrenheit > 0:
        new_temperature = (fahrenheit - 32) * 5/9
    return new_temperature


main()
