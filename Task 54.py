class Rectangle():
    __width = 0
    __height = 0

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def getSquare(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * self.__width + 2 * self.__height

    def getRatio(self):
        return self.getSquare() / self.getPerimeter()

rectangle = Rectangle(11, 11)
print(rectangle.getSquare())
print(rectangle.getPerimeter())
print(rectangle.getRatio())
