#Tail Recursion
def PrintPattern(num):
    print("Inside Tail")
    if num != 0:
        print("*", end=" ")
        num = num - 1
        PrintPattern(num)

#Head Recursion
def PrintPattern(num):
    #print("Inside Head")
    if num != 0 :
        num = num - 1
        PrintPattern(num)
        print("*", end=" ")

def main():
    num = int(input("Enter a number: "))
    PrintPattern(num)

if __name__ == "__main__":
    main()