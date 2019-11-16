def PrintPattern(no):
    if no != 0:
        no -= 1
        PrintPattern(no)
        print(no+1, end=" ")

def main():
    no = int(input("Enter a number: "))
    PrintPattern(no)

if __name__ == "__main__":
    main()