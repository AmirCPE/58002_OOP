import math


class Circle:
    def __init__(self):
        self.radius = 0.0
        self.diameter = 0.0

    def get_radius(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def get_diameter(self):
        self.diameter = float(input("Enter the diameter of the circle: "))
        self.radius = self.diameter / 2.0

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
c = Circle()
c.get_radius()
print("Area of the circle: ", c.area())
print("Perimeter of the circle: ", c.perimeter())

c.get_diameter()
print("Area of the circle: ", c.area())
print("Perimeter of the circle: ", c.perimeter())
