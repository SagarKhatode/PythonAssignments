class Arithmatic:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if (self.Value > 1):
            for i in range(2, self.Value):
                if (self.Value % i) == 0:
                    return False
            else:
                return  True
        else:
            return False

    def ChkPerfect(self):
        if self.Value > 0:
            Sum = 0
            for i in range(1, self.Value):
                if self.Value % i == 0:
                   Sum = Sum + i
            if self.Value == Sum:
                return True
            else:
                return False
        else:
            return False

    def Factors(self):
        if self.Value > 0:
            FactorsList = list()
            for i in range(1, self.Value):
                if self.Value % i == 0:
                    FactorsList.append(i)
            print("Factors of {0} is {1}".format(self.Value, FactorsList))
            return FactorsList
        else:
            print("Provided number does not have any factors")

    def SumFactors(self):
        FactorsLst = self.Factors()
        Sum = 0

        if len(FactorsLst) > 0:
            for i in range(len(FactorsLst)):
                Sum = Sum + FactorsLst[i]
            return Sum

def main():
    obj1 = Arithmatic(6)
    print("Number {0} is prime: {1}".format(obj1.Value, obj1.ChkPrime()))
    print("Number {0} is Perfect: {1}".format(obj1.Value, obj1.ChkPerfect()))
    obj1.Factors()
    print("Sum of Factors: {}".format(obj1.SumFactors()))

if __name__ == "__main__":
    main()


