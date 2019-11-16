def ChkPrime(Num):
	if Num > 1:
		for i in range(2, Num):
			if Num % i == 0:
				break
				return False
		else:
			return True
	else:
		return False