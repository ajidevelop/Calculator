import special_operations as so

def solveX(c, n, a, o):
	if (o == "*" or o == "multiply" or o == "times" or o == "time") :
		multiplier_result = a / (c*n)
		return multiplier_result
	elif (o == "/" or o == "divide"):
		numerator = input("Is x on the numerator: ")
		if (numerator == "Y" or numerator == "y" or numerator == "Yes" or numerator == "yes"):
			divisor_result = (a * n) / c
		elif (numerator == "N" or numerator == "n" or numerator == "No" or numerator == "no"):
			divisor_result = n/(a * c)
		print(divisor_result)
	elif (o == "+" or o == "add"):
		addition_result = (a - n) / c
		print(addition_result) 
	elif (o == "-" or o == "minus" or o == "subtract"):
		subtraction_result = (a + n) / c
		print(subtraction_result)


def solveXexp(c, n, a):
	"""c =""" 