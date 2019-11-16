class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self, Radius):
        self.Radius = Radius

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius: {}".format(self.Radius))
        print("Area: {}".format(self.Area))
        print("Circumference: {}".format(self.Circumference))


def main():
    rad = int(input("Enter radius of the circle: "))
    obj1 = Circle()
    obj1.Accept(rad)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    print("Details of Circle: ")
    obj1.Display()


if __name__ == "__main__":
    main()