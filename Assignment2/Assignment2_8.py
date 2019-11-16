def pattern(num):
	i = 1
	while i <= num:
		for x in range(i):
			print((x+1), end = " ")
		print()
		i += 1
if __name__ == '__main__':
	num = int(input("Enter a number: "))
	pattern(num)