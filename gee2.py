class Polygon:
    # width = int(input("Please enter a number: "))
    # height = int(input("Please enter a value: "))
    __width = None
    __height = None

    def set_value(self, width, height):
        self.__width = width
        self.__height = height


    def get_width(self):
        return self.__width


    def get_height(self):
        return self.__height



class Rectangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width()


rec = Rectangle()
rec.set_value(4, 6)
print(rec.area())



