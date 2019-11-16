def addDigits(num):
	sum = 0
	while num > 0:
		sum = sum + (num%10)
		num = num // 10
	print("Addition of digits: ", sum)
if __name__ == '__main__':
	num = int(input("Enter a number: "))
	addDigits(num)