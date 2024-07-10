"""work2.py"""

class Ship:
    def __init__(self, name, country, displacement):
        self.__name = name
        self.__country = country
        self.__displacement = displacement

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_country(self, country):
        self.__country = country

    def get_country(self):
        return self.__country

    def set_displacement(self, displacement):
        self.__displacement = displacement

    def get_displacement(self):
        return self.__displacement

    def display_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Country: {self.get_country()}")
        print(f"Displacement: {self.get_displacement()} tons")


class Frigate(Ship):
    def __init__(self, name, country, displacement, armament):
        super().__init__(name, country, displacement)
        self.__armament = armament

    def set_armament(self, armament):
        self.__armament = armament

    def get_armament(self):
        return self.__armament

    def display_info(self):
        super().display_info()
        print(f"Armament: {self.get_armament()}")


class Destroyer(Ship):
    def __init__(self, name, country, displacement, speed):
        super().__init__(name, country, displacement)
        self.__speed = speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def display_info(self):
        super().display_info()
        print(f"Speed: {self.get_speed()} knots")


class Cruiser(Ship):
    def __init__(self, name, country, displacement, range):
        super().__init__(name, country, displacement)
        self.__range = range

    def set_range(self, range):
        self.__range = range

    def get_range(self):
        return self.__range

    def display_info(self):
        super().display_info()
        print(f"Range: {self.get_range()} nautical miles")


if __name__ == "__main__":
    frigate = Frigate("USS Freedom", "USA", 3500, "Missiles, Torpedoes")
    frigate.display_info()

    destroyer = Destroyer("USS Arleigh Burke", "USA", 9200, 31)
    destroyer.display_info()

    cruiser = Cruiser("USS Ticonderoga", "USA", 9800, 6000)
    cruiser.display_info()
