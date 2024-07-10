"""work1.py"""

class Device:
    def __init__(self, brand, model, power):
        self.__brand = brand
        self.__model = model
        self.__power = power

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_power(self, power):
        self.__power = power

    def get_power(self):
        return self.__power

    def display_info(self):
        print(f"Brand: {self.get_brand()}")
        print(f"Model: {self.get_model()}")
        print(f"Power: {self.get_power()}W")


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_tank_capacity):
        super().__init__(brand, model, power)
        self.__water_tank_capacity = water_tank_capacity

    def set_water_tank_capacity(self, capacity):
        self.__water_tank_capacity = capacity

    def get_water_tank_capacity(self):
        return self.__water_tank_capacity

    def display_info(self):
        super().display_info()
        print(f"Water Tank Capacity: {self.get_water_tank_capacity()}L")


class Blender(Device):
    def __init__(self, brand, model, power, speed_settings):
        super().__init__(brand, model, power)
        self.__speed_settings = speed_settings

    def set_speed_settings(self, settings):
        self.__speed_settings = settings

    def get_speed_settings(self):
        return self.__speed_settings

    def display_info(self):
        super().display_info()
        print(f"Speed Settings: {self.get_speed_settings()}")


class MeatGrinder(Device):
    def __init__(self, brand, model, power, blade_material):
        super().__init__(brand, model, power)
        self.__blade_material = blade_material

    def set_blade_material(self, material):
        self.__blade_material = material

    def get_blade_material(self):
        return self.__blade_material

    def display_info(self):
        super().display_info()
        print(f"Blade Material: {self.get_blade_material()}")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine("DeLonghi", "ECAM22.110", 1450, 1.8)
    coffee_machine.display_info()

    blender = Blender("Philips", "HR3556", 700, 5)
    blender.display_info()

    meat_grinder = MeatGrinder("Bosch", "MFW67440", 2000, "Stainless Steel")
    meat_grinder.display_info()
