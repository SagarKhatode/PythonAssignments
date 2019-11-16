def listAddition(num):
	Arr = list()
	for i in range(0, num):
		print("No ",i,":")
		Arr.append(int(input()))
	print("Max: ", max(Arr))

def main():
	num = int(input("Enter number of elements: "))
	listAddition(num)

if __name__ == '__main__':
	main()