from polygon import Polygon, Triangle, Quadilateral


class Area:
    "To calculate area of plane shapes"

    def __init__(self, *args, number=0, length_of_side=0):
        """For Polygons pass 2 argument : number of sides and the length.
        this program is unable to calculate irregular polygons.
        For other shapes just pass the sides individually"""
        self.sides = None
        if args:
            self.sides = args
        
        self.number = number
        self.length = length_of_side
    
    def return_area(self):
        if self.sides:
            if len(self.sides) == 3:
                return Triangle(self.sides).print_area()
            elif len(self.sides) == 4:
                return Quadilateral(self.sides).print_area()
        if self.number and self.length:
            return Polygon((self.number, self.length)).print_area()



    

