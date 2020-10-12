from Prac_08.unreliable_car import Unreliable_Car


def main():
    new_car = Unreliable_Car("Mustang", 100, 70)
    for index in range(1, 10):
        new_car.drive(10)


main()
