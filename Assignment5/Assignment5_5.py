fact = 1
def Factorial(no):
    global fact
    if no != 0:
        fact = fact * no
        no -= 1
        Factorial(no)

def main():
    no = int(input("Enter a number: "))
    Factorial(no)
    print("Factorial of {0} is {1}".format(no, fact))

if __name__ == "__main__":
    main()