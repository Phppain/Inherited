"""task2.py"""

class Wheels:
    def __init__(self, number_of_wheels, wheel_type):
        self.number_of_wheels = number_of_wheels
        self.wheel_type = wheel_type

    def set_number_of_wheels(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def get_number_of_wheels(self):
        return self.number_of_wheels

    def set_wheel_type(self, wheel_type):
        self.wheel_type = wheel_type

    def get_wheel_type(self):
        return self.wheel_type

    def display_info(self):
        print(f"Number of wheels: {self.get_number_of_wheels()}")
        print(f"Wheel type: {self.get_wheel_type()}")


class Engine:
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def set_engine_type(self, engine_type):
        self.engine_type = engine_type

    def get_engine_type(self):
        return self.engine_type

    def set_horsepower(self, horsepower):
        self.horsepower = horsepower

    def get_horsepower(self):
        return self.horsepower

    def display_info(self):
        print(f"Engine type: {self.get_engine_type()}")
        print(f"Horsepower: {self.get_horsepower()} HP")


class Doors:
    def __init__(self, number_of_doors, door_type):
        self.number_of_doors = number_of_doors
        self.door_type = door_type

    def set_number_of_doors(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def get_number_of_doors(self):
        return self.number_of_doors

    def set_door_type(self, door_type):
        self.door_type = door_type

    def get_door_type(self):
        return self.door_type

    def display_info(self):
        print(f"Number of doors: {self.get_number_of_doors()}")
        print(f"Door type: {self.get_door_type()}")


class Car(Wheels, Engine, Doors):
    def __init__(self, number_of_wheels, wheel_type, engine_type, horsepower, number_of_doors, door_type):
        Wheels.__init__(self, number_of_wheels, wheel_type)
        Engine.__init__(self, engine_type, horsepower)
        Doors.__init__(self, number_of_doors, door_type)

    def display_info(self):
        print("Car details:")
        Wheels.display_info(self)
        Engine.display_info(self)
        Doors.display_info(self)


if __name__ == "__main__":
    car = Car(4, "All-season", "V8", 450, 4, "Sedan")
    car.display_info()
