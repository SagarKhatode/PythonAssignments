def PrintPattern(no):
    if no != 0:
        print(no, end=" ")
        no -= 1
        PrintPattern(no)

def main():
    no = int(input("Enter a number: "))
    PrintPattern(no)

if __name__ == "__main__":
    main()