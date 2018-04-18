import numpy as np
import variables as var
import special_operations as so
import sys


Number = []
cont = True
print("Welcome to Kevin's Calculator")
result = 0
i = 0

def calc():

	operator = input("What operator should be used: ")
	if (operator == "solveX"):
		c = float(input("coefficient of x: "))
		n = float(input("integer: "))
		a = float(input("answer: "))
		o = input("opertaor: ")
		print(str(c) + "x " + o + " " + str(n) + " = " + str(a))
		print(var.solveX(c, n, a, o))
	
	numb1 = ""
	numb2 = ""

	if (operator != "solveX"):
		if (operator == "factorial" or "!"):
			numb1 = input("Enter a number: ")
		else:
			numb1 = input("Enter first number: ")
			numb2 = input("Enter second numeber: ")
	try:
		number1 = float(numb1)
	except ValueError:
		number1 = ""
	try:
		number2 = float(numb2)
	except ValueError:
		number2 = ""


	if (operator == "end" or number1 == "end" or number2 == "end"):
		sys.exit()
	
	if (operator == "*" or operator == "multiply" or operator == "times" or operator == "time") :
		result_mult = number1 * number2
		print(result_mult)
	elif (operator == "/" or operator == "divide"):
		if (number2 == 0):
			print("Undefined, Denominator cannot have 0")
		else:
			result_div = number1 / number2
			print(result_div)
	elif (operator == "+" or operator == "add"):
		result_add = number1 + number2
		if ((number1 == 9 and number2 == 10) or (number1 == 10 and number2 == 9)):
			result910 = "21"
			print(result910)	
		else:
			print(result_add)
	elif (operator == "-" or operator == "minus" or operator == "subtract"):
		result_min = number1 - number2
		if (number1 > number2):
			print(result_min)
		elif (number2 > number1):
			negative = str(result_min)
			print(negative)
	elif (operator == "^" or operator == "exponent"):
		result_exp = number1 ** number2
		print(result_exp)
	elif (operator == "root"):
		result_root = number1 ** (1/number2)
		print(result_root)
	elif (operator == "log"):
		print(so.log(number1, number2))
	elif (operator == "!" or "factorial"):
		print(so.factorials(number1))

calc()

more_calc = True
while(more_calc == True):
	more_calc = input("Would you like to continue (Y/N):")
	if (more_calc == "Y" or more_calc == "y" or more_calc == "Yes" or more_calc == "yes"):
		calc()
		more_calc = True
	elif (more_calc == "N" or more_calc == "n" or more_calc == "No" or more_calc == "no" or "end"):
		more_calc = False
		break
