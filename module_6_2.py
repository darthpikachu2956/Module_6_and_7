class Vehicle:
    __COLOR_VARIANTS = ['white', 'black', 'red', 'blue', 'green', 'yellow']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.set_color(color)

    def get_model(self):
        return f'Model: {self.__model}'

    def get_horsepower(self):
        return f'Engine power: {self.__engine_power}'

    def get_color(self):
        return f'Color: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}')
        print(f'{self.get_horsepower()}')
        print(f'{self.get_color()}')
        print(f'The owner of the car: {self.owner}\n')

    def set_color(self, new_color):
        lower_color = new_color.lower()
        if lower_color in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'You cannot change the color to {new_color}!\n')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def get_limit(self):
        print(f'The passengers limit in this car is {self.__PASSENGERS_LIMIT}.\n')


vehicle1 = Sedan('Sweet', 'Groove', 300, 'blue')
vehicle1.print_info()

vehicle1.get_limit()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'CJ'
vehicle1.print_info()
