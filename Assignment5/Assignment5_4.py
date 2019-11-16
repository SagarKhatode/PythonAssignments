sum = 0
def PrintSummationOfDigits(no):
    global sum
    if no != 0:
        val = no%10
        no = no//10
        sum += val
        strng = str(val)
        if no != 0:
            strng += "+"
        print(strng, end="")
        PrintSummationOfDigits(no)

def main():
    no = int(input("Enter a number: "))
    PrintSummationOfDigits(no)
    print("  ==>  Summation is: {}".format(sum))


if __name__ == "__main__":
    main()