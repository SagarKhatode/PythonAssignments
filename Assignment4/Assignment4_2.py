Fptr = lambda no1, no2 : no1 * no2

def main():
	no1 = int(input("Enter 1st Number: "))
	no2 = int(input("Enter 2nd Number: "))
	print("Multiplication of {0} and {1} is: {2}".format(no1, no2, Fptr(no1, no2)))

if __name__ == "__main__":
	main()