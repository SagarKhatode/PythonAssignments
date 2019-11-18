import threading
import multiprocessing
import os

def Even():
    print("Process of Even: ", os.getpid())
    print("Process of parent of Even: ", os.getppid())
    print("Even Numbers: ")
    for i in range(1, 10):
        if i % 2 ==0:
            print("Even",i)

def Odd():
    print("Process of odd: ", os.getpid())
    print("Process of parent of Odd: ", os.getppid())
    print("Odd Numbers: ")
    for i in range(1, 10):
        if i % 2 != 0:
            print("Odd",i)


def main():
    print("Process of parent of main: ", os.getppid())
    print("Prosess ID of main: ", os.getpid())

    even = threading.Thread(target=Even)
    odd = threading.Thread(target=Odd)
    even.start()
    odd.start()
    even.join()
    odd.join()

    print("Exit from main")


if __name__ == '__main__':
    main()