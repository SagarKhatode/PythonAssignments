def pattern(num):
	for y in range(num):
		for x in range(num):
			print((x+1), end = " ")
		print()
if __name__ == '__main__':
	num = int(input("Enter a number: "))
	pattern(num)