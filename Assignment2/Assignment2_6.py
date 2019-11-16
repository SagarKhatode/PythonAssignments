def pattern(num):
	gum = num
	while gum >= 1:
		num = gum
		while num >= 1:
			print("*", end = " ")
			num -= 1
		print()
		gum -= 1

if __name__ == '__main__':
	num = int(input("Enter a number: "))
	pattern(num)