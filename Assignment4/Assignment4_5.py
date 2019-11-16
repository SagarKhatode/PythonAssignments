def ChkPrime(no):
	if no > 1:
		for i in range(2, no):
			if no % i == 0:
				break
				return False
		else:
			return True
	else:
		return False

def main():
	no = int(input("Enter a number: "))
	if no > 0:
		Arr = list()
		for i in range(0, no):
			print("Enter no {}: ".format(i+1), end="")
			Arr.append(int(input()))
		print("Accepted List: {}".format(Arr))
		FilteredList = list(filter(ChkPrime, Arr))
		if len(FilteredList) > 0:
			print("Filtered List: {}".format(FilteredList))
			MappedList = list(map(lambda no : no * 2, FilteredList))
			print("Mapped list: {}".format(MappedList))
			print("Maximum number from mapped list is: {}".format(max(MappedList)))
		else:
			print("There is no filtered data for further operations")
	else:
		print("Please enter a valid number")
if __name__ == "__main__":
	main()