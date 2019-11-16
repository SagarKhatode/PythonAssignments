import Arithmatic

def ArithmaticOperations(num1, num2):
	print("Addition is: ", Arithmatic.Add(num1, num2))
	
	print("Substraction is: ", Arithmatic.Sub(num1, num2))
	
	print("Multiplication is: ", Arithmatic.Mul(num1, num2))
	
	print("Division is: ", Arithmatic.Div(num1, num2))

if __name__ == '__main__':
	print("Enter num1: ")
	num1 = input()
	print("Enter num2: ")
	num2 = input()
	ArithmaticOperations(num1, num2)