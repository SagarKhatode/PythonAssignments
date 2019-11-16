class Demo:
    value = 10

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def fun(self):
        print("NO1: ", self.no1, end=" ")
        print("NO2: ", self.no2)

    def gun(self):
        print("NO1: ", self.no1, end=" ")
        print("NO2: ", self.no2)

    @classmethod
    def Sun(cls, val):
        print("Value: {}".format(cls.value + val))

def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(21, 101)
    obj1.fun()
    obj2.gun()
    obj1.fun()
    obj2.gun()
    Demo.Sun(15)

if __name__ == "__main__":
    main()