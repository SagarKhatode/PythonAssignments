from MarvellousNum import *
from functools import *
def ListPrime(Num):
	Arr = list()
	for i in range(0, Num):
		print("Enter No ",i+1," :")
		Arr.append(int(input()))
	PrimeList = list(filter(ChkPrime, Arr))
	print("Arr: ",Arr)
	print(PrimeList)
	numberList = ""
	for i in PrimeList:
		numberList = numberList + "+" + str(i)
	print("Output: ", reduce(lambda no1, no2: no1+no2, PrimeList),"(",numberList,")")

def main():
	Num = int(input("Enter number of elements: "))
	ListPrime(Num)

if __name__ == "__main__":
	main()