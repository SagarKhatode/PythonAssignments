def factorAdd(num):
	sum = 0
	for x in range(num):
		if x == 0:
			continue
		if num % x == 0:
			sum += x
	return sum
if __name__ == "__main__":
	num = int(input("Enter a number: "))
	print("Addition of ",num," factors: ", factorAdd(num))