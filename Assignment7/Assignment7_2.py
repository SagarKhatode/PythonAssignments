class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Deposit(self, Amt):
        self.Amount = self.Amount + Amt

    def Withdraw(self, Amt):
        if self.Amount > Amt:
            self.Amount = self.Amount - Amt
        else:
            print("Insufficient Balance")
    def CalculateInt(self):
        return (self.Amount * BankAccount.ROI)/100

    def Display(self):
        print("Name: ", self.Name)
        print("Amount: ",self.Amount)
        print("Interest Rate: ", self.CalculateInt())

def main():
    obj1 = BankAccount("Sagar", 5000)
    obj1.Deposit(5000)
    obj1.Withdraw(500)
    obj1.Display()

    obj2 = BankAccount("Sanket", 10000)
    obj2.Deposit(500)
    obj2.Withdraw(2000)
    obj2.Display()

if __name__ == "__main__":
    main()