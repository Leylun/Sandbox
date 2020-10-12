from Prac_08.silver_service_taxi import Silver_Service_Taxi
from Prac_08.Taxi import Taxi


def main():
    taxis = [Taxi("Prius", 100), Silver_Service_Taxi("Limo", 100, 2), Silver_Service_Taxi("Hummer", 200, 4)]
    current_taxi = None
    current_fare = 0
    print("Let's Drive!")
    while True:
        user_input = input("q)uit, c)hoose taxi, d)rive").upper()
        if user_input == "Q":
            print("Total trip cost: {:.2f}".format(current_fare))
            print("Taxis are now:")
            for taxi in taxis:
                print(taxi)
            quit()
        elif user_input == "C":
            print("Taxis available:")
            index = 0
            for taxi in taxis:
                print("{} - {}".format(index, taxi))
                index += 1
            while True:
                try:
                    user_taxi = int(input("Choose taxi:"))
                except TypeError:
                    continue
                else:
                    if -1 < user_taxi < len(taxis):
                        current_taxi = taxis[user_taxi]
                        break
        elif user_input == "D":
            if current_taxi is not None:
                while True:
                    try:
                        user_distance = int(input("Drive how far?"))
                    except TypeError:
                        continue
                    else:
                        current_taxi.drive(user_distance)
                        break
                current_fare += current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_fare))
        print("Bill to date: ${:.2f}".format(current_fare))


main()
