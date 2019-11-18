import threading

def Thread1():
    for i in range(1, 5115):
        print("Thread1 ", i)

def Thread2():
    for i in range(1, 5115):
        print("Thread2 ", (51-i))

def main():
    thread1 = threading.Thread(target=Thread1)
    thread2 = threading.Thread(target=Thread2)

    thread1.start()
    thread1.join()
    thread2.start()

    thread2.join()
    print("End of main")

if __name__ == '__main__':
    main()