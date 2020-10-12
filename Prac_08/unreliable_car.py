from Prac_08.Car import Car
from random import randint


class Unreliable_Car(Car):

    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.distance = 0

    def drive(self, distance):
        chance = randint(1, 100)
        if chance < self.reliability:
            self.distance = distance
        else:
            print("Car Broke")
        return distance
