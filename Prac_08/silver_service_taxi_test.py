from Prac_08.silver_service_taxi import Silver_Service_Taxi


def main():
    new_car = Silver_Service_Taxi("Hummer", 200, 2)
    print(new_car)
    new_car.drive(18)
    print("${}".format(new_car.get_fare()))


main()
