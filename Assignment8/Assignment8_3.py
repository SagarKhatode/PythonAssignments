import threading
def EvenList(list):
    if len(list) > 0:
        sum = 0
        for i in range(len(list)):
            if list[i] % 2 == 0:
                sum = sum + list[i]
        print("Sum of Even numbers in list: ", sum)

def OddList(list):
    if len(list) > 0:
        sum = 0
        for i in range(len(list)):
            if list[i] % 2 != 0:
                sum = sum + list[i]
        print("Sum of odd numbers in list: ", sum)

def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    evenlist = threading.Thread(target = EvenList, args=(lst,))
    oddlist = threading.Thread(target=OddList, args=(lst,))

    evenlist.start()
    oddlist.start()


if __name__ == '__main__':
    main()