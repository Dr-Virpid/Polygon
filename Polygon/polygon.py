import abc
import math



class Shape(metaclass=abc.ABCMeta):

    def __init__(self, args):
        self.sides = args
    
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractproperty
    def types(self):
        pass

    def print_area(self):
        area_n_shape = self.calculate_area()
        if area_n_shape:
            return f"The area of the {area_n_shape[1]} is {area_n_shape[0]} cm" 
        return f"This is not a {self.__class__.__name__}"


class Triangle(Shape):
    types = {1: "Equilateral Triangle",
            2: "Isoceles Triangle",
            3: "Scalene Triangle",
            4: "Right-angle Triangle"}

    def calculate_area(self):
        d = set(self.sides)
        d = list(d)  # sets do not support indexing or slicing
        if len(d) == 1:
            area = (math.sqrt(3) * d[0]**2) / 4
            return (area, self.types[1])
        if len(d) == 2:
            d = sorted(list(self.sides))  # converts the tuple to a list then sorts it
            if d[0] == d[1]:  # checks which of the element of the list is identical then uses it to calculate area of triangle
                area = 1/2 * d[2] * math.sqrt((d[0]**2)- (d[2]**2 / 4))
            elif d[0] == d[2]:
                area = 1/2 * d[1] * math.sqrt((d[0]**2)- (d[1]**2 / 4))
            else:
                area = 1/2 * d[0] * math.sqrt((d[1]**2)- (d[0]**2 / 4))
            return (area, self.types[2])
        if len(d) == 3:
            area = 0.25 * math.sqrt(d[0] + d[1] + d[2]) *  math.sqrt(-d[0] + d[1] + d[2]) *  math.sqrt(d[0] - d[1] + d[2]) *  math.sqrt(d[0] + d[1] - d[2])
            d = sorted(list(self.sides))
            if d[-1] **2 == d[-2]**2 + d[-3] ** 2:
                return (area, self.types[4])
            return (area, self.types[3])



class Quadilateral(Shape):
    types = ("Square", "Rectangle",)

    def calculate_area(self):
        d = set(self.sides)
        if len(d) == 1:
            area = self.sides[0]**2
            return (area, self.types[0])
        elif len(d) == 2:
            area = self.sides[0] * self.sides[1]
            return (area, self.types[1])
        return False
    

class Polygon(Shape):
    types = {
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Nonagon",
        10: "Decagon"
    }
    

    def calculate_area(self):
        number = self.sides[0]
        length = self.sides[1]
        area = (length**2 * number) / (4 * math.tan(180/number))
        return (area , self.types[number])

        





            