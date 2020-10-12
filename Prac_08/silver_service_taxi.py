from Prac_08.Taxi import Taxi


class Silver_Service_Taxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness
        self.flag_fall = 4.50

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flag_fall
