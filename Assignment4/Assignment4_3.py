from functools import *
def filterData(no):
	if no>=70 and no<=90:
		return True
	else:
		return False

def mapOperation(no):
	return no+10

def multiplication(no1, no2):
	return no1*no2


def main():
	Arr = list()
	no = int(input("Enter a number: "))
	for i in range(0,no):
		print("Enter number {} : ".format(i+1))
		inputNumber = int(input())
		Arr.append(inputNumber)
	print("Accepted List: {}".format(Arr))
	FilteredData = list(filter(filterData, Arr))
	print("Filtered Data: {}".format(FilteredData))
	if len(FilteredData) > 0:
		MapData = list(map(mapOperation,FilteredData))
		print("Mapped Data : {}".format(MapData))
		print("Output of Reduce: {}".format(reduce(multiplication, MapData)))
	else:
		print("There is no filtered data for further operations")

if __name__ == '__main__':
	main()