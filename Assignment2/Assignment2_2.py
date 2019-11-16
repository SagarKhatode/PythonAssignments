def printPattern(num):
	i = 1
	while i <= int(num):
		j = 1
		while j <= int(num):
			print("*", end = " ")
			j += 1
		print()
		i += 1
if __name__ == '__main__':
	print("Enter number: ")
	printPattern(input())