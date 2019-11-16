from functools import *
def listAddition(num):
	Arr = list()
	for i in range(num):
		print("No ",(i+1),":", end="")
		Arr.append(int(input()))
	print("Addition of Arr: ",reduce(lambda no1, no2: no1 + no2,Arr))

def main():
	num = int(input("Enter number of elements: "))
	listAddition(num)

if __name__ == '__main__':
	main()