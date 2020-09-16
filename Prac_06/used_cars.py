"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo)


main()
