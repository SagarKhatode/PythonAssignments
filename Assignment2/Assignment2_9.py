def numberOfDigits(num):
	count = 0
	while num > 0:
		num = num // 10
		count += 1
	print("Number of digits: ", count)
if __name__ == "__main__":
	num = int(input("Enter a number: "))
	numberOfDigits(num)