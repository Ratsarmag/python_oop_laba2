class Circle():
    __radius = 0

    def __init__(self, radius):
        self.__radius = radius

    def getSquare(self):
        return 3.14 * self.__radius ** 2

    def getCircleLength(self):
        return 2 * 3.14 * self.__radius

circle = Circle(7)

print(circle.getSquare())
print(circle.getCircleLength())
