class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        coordinates = (self.x_distance, self.y_distance)
        return coordinates

    def voice(self):
        print(self.sound)


centaurus = Pegasus()

print(centaurus.get_pos())
centaurus.move(10, 15)
print(centaurus.get_pos())
centaurus.move(-5, 20)
print(centaurus.get_pos())

centaurus.voice()
