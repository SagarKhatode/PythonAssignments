def factorial(num):
	if num == 1:
		return num
	else:
		return num * factorial(num - 1)
if __name__ == "__main__":
	num = int(input("Enter a number: "))
	if num < 0:
		print("The factorial of negative number does not exist")
	elif num == 0:
		print("Factorial of 0 is 1")
	else:
		print("Factorial is: ", factorial(num))
