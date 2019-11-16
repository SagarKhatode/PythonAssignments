class BookStore:

    NoOfBooks = 0

    def __init__(self, Name, Auther):
        self.Name = Name
        self.Auther = Auther
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.Name, "by", self.Auther, "No of books: ", BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritche")
    obj2.Display()

if __name__ == "__main__":
    main()