from functools import *
def main():
	no = int(input("Enter a number: "))
	if no > 0:
		Arr = list()
		for i in range(0, no):
			print("Enter no {}: ".format(i+1))
			Arr.append(int(input()))
		FilteredList = list(filter(lambda no : not(no%2), Arr))
		print("Filtered List: {}".format(FilteredList))
		if len(FilteredList) > 0:
			SquareList = list(map(lambda no : no**2, FilteredList))
			print("Square of numbers in list: {}".format(SquareList))
			print("Addition of all numbers in list: {}".format(reduce(lambda no1, no2 : no1 + no2, SquareList)))

if __name__ =="__main__":
	main()