def CalculateFreq(Num):
	Arr = list()
	for i in range(Num):
		print("Enter no ", (i+1) , ": ")
		Arr.append(int(input()))
	no = int(input("Enter number to search: "))
	count = 0
	for i in range(len(Arr)):
		if Arr[i] == no:
			count += 1
	print("List Arr is: ", Arr)
	print("Occurance of ", no, " in list Arr is: ", count)

def main():
	Num = int(input("Enter number of elements: "))
	CalculateFreq(Num)

if __name__ == "__main__":
	main()