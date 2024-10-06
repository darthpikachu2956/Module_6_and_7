import math


class Figure:
    sides_count = 0

    def __init__(self, sides, color):
        self.__sides = sides  # List of sides' lengths
        if sides != self.sides_count:
            self.__sides = [sides[0]] * self.sides_count
        self.__color = color
        self.filled = True

    def get_color(self):  # returns the color
        return self.__color

    def __is_valid_color(self, r, g, b):  # checks if the color is correct
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
        return False

    def set_color(self, r, g, b):  # changes the color
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print("Such color doesn't exist!")

    def __is_valid_sides(self, *args):  # checks if the sides number is correct
        if len(self.__sides) == len(args) and all(isinstance(side, int) for side in self.__sides):
            return True
        return False

    def get_sides(self):  # returns the sides
        return self.__sides

    def __len__(self):  # counts the sum of sides' length
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # changes the sides
        if len(new_sides) != self.sides_count:
            print("Wrong number of sides for the figure!")
            return
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


#############################################
class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color):
        super().__init__(sides, color)
        self.__radius = len(self) / (2 * math.pi)

    def set_sides(self, *new_sides):  # Updating method of parent
        super().set_sides(*new_sides)  # Updating sides
        self.__radius = len(self) / (2 * math.pi)  # Updating radius

    def get_square(self):
        sqr = math.pi * self.__radius ** 2
        return sqr


#############################################
class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color):
        super().__init__(sides, color)
        self.__sides = sides

    def get_square(self):
        my_list = []
        s = sum(self.__sides) / 2  # Half perimeter
        for i in self.__sides:
            elem = s - i  # Calculating elements for Heron formula
            my_list.append(elem)
        almost_result = 1
        for j in my_list:
            almost_result *= j  # Multiplying 1 on each element of my list altogether
        sqr = math.sqrt(almost_result * s)
        return sqr


#############################################
class Cube(Figure):
    sides_count = 12

    def __init__(self, sides, color):
        self.__sides = [sides[0]] * Cube.sides_count
        super().__init__(self.__sides, color)

    def get_volume(self):
        volume = self.__sides[0] ** 3
        return volume


#############################################
    # Testing getting and setting colors and sides for Figure
# fig1 = Figure([1, 1, 1], (0, 255, 0))
# color1 = fig1.get_color()
# print(color1)
# fig1.set_color(150, 150, 200)
# color1 = fig1.get_color()
# print(color1)

# side1 = fig1.get_sides()
# print(side1)
# fig1.set_sides(3, 3, 4)
# side1 = fig1.get_sides()
# print(side1)
#############################################
print()
print("======================= Testing Circle =======================")
cir1 = Circle([5], (155, 155, 100))

print(cir1.get_color())
cir1.set_color(200, 200, 200)
print(cir1.get_color())
cir1.set_color(300, 300, 300)
print(cir1.get_color())
print()

# print(cir1.radius)  # Just checked if radius worked
print(f"If the circle length = {cir1.get_sides()}, the square is {round(cir1.get_square(), 2)}")
cir1.set_sides(12)
# print(cir1.radius)  # Just checked if radius changed
print(f"If the circle length = {cir1.get_sides()}, the square is {round(cir1.get_square(), 2)}")
#############################################
print()
print("======================= Testing Triangle =======================")
tri1 = Triangle([4, 4, 4], (200, 200, 200))
# (4 + 4 + 4) / 2 = 6
# print(6*(6-4)*(6-4)*(6-4))
# print(round(math.sqrt(48), 2))  # Checked the square manually, just in case, to compare with my cycles
print(f"If the triangle sides are {tri1.get_sides()}, the square is {round(tri1.get_square(), 2)}")
print(f"The sum of triangle's sides is {len(tri1)}")
tri1.set_sides(1, 2, 2, 3)
print(f"The triangle's sides are still {tri1.get_sides()}")
#############################################
print()
print("======================= Testing Cube =======================")

cube1 = Cube([3], (200, 200, 200))
print(f"The cube's perimeter is {len(cube1)}")
print(f"The cube's volume is {cube1.get_volume()}")
#############################################
print()
print("======================= Triangle again if incorrect sides when created =======================")
tri2 = Triangle([4, 4, 4, 4, 4], (200, 200, 200))
print(tri2.get_sides())
