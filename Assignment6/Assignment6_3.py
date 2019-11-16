class Arithmatic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value1: "))
        self.Value2 = int(input("Enter Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2

def main():
    obj1 = Arithmatic()
    obj1.Accept()
    print("Arithmatic Operations:- ")
    print("Addition: ",obj1.Addition(), "Substraction: ", obj1.Substraction())
    print("Multiplication: ", obj1.Multiplication(), "Division: ", obj1.Division())

    obj2 = Arithmatic()
    obj2.Accept()
    print("Arithmatic Operations:- ")
    print("Addition: ", obj2.Addition(), "Substraction: ", obj2.Substraction())
    print("Multiplication: ", obj2.Multiplication(), "Division: ", obj2.Division())
if __name__ == "__main__":
    main()