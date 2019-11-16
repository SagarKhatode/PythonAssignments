Fptr = lambda no: no**2
def main():
	no = int(input("Enter a number: "))
	print("Square of {0} is {1}".format(no, Fptr(no)))

if __name__ == "__main__":
	main()