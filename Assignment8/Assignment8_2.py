import threading
import os
def EvenFactor(Value):
    sum = 0
    if Value > 0:

        for i in range(1, Value):
            print("EvenFact")
            if Value % i == 0:
                if i % 2 ==0:
                    sum = sum + i
        print("EvenFactor: ",sum)

def OddFactor(Value):
    sum = 0
    if Value > 0:
        for i in range(1, Value):
            print("OddFact")
            if ((Value % i) == 0):
                if i % 2 != 0:
                    sum = sum + i
        print("OddFactor: ",sum)

def main():

    evenfactor = threading.Thread(target=EvenFactor, args=(1000,))
    oddfactor = threading.Thread(target=OddFactor, args=(500,))
    evenfactor.start()
    oddfactor.start()
    print("End of main")

if __name__ == '__main__':
    main()