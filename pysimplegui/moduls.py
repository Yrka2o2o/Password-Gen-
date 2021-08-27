import string
from random import choice

az = string.ascii_lowercase
AZ = string.ascii_uppercase
spec_sumbol = string.punctuation
digits = string.digits

val_pass = ["pass", "pass", "pass"]

def generate_pass(len_pass, sumbol):
	password = []
	list(sumbol)
	i = 0
	while i < len_pass:
		s = choice(sumbol)
		password.append(s)
		i += 1
	return "".join(password)

def check_checkbox(len_pass, values):
	# Если нажат только один из 4 чекбоксов
	if values[0] == True and values[1] == False and values[2] == False and values[3] == False:
		val = generate_pass(len_pass, az)

	elif values[0] == False and values[1] == True and values[2] == False and values[3] == False:
		val = generate_pass(len_pass, AZ)

	elif values[0] == False and values[1] == False and values[2] == True and values[3] == False:
		val = generate_pass(len_pass, spec_sumbol)

	elif values[0] == False and values[1] == False and values[2] == False and values[3] == True:
		val = generate_pass(len_pass, digits)

	# Варианты нажатий 2 чекбокса из 4
	elif values[0] == True and values[1] == True and values[2] == False and values[3] == False:
		val = generate_pass(len_pass, az+AZ)

	elif values[0] == True and values[1] == False and values[2] == True and values[3] == False:
		val = generate_pass(len_pass, az+spec_sumbol)

	elif values[0] == True and values[1] == False and values[2] == False and values[3] == True:
		val = generate_pass(len_pass, az+digits)

	elif values[0] == False and values[1] == True and values[2] == True and values[3] == False:
		val = generate_pass(len_pass, AZ+spec_sumbol)

	elif values[0] == False and values[1] == True and values[2] == False and values[3] == True:
		val = generate_pass(len_pass, AZ+digits)

	elif values[0] == False and values[1] == False and values[2] == True and values[3] == True:
		val = generate_pass(len_pass, spec_sumbol+digits)

	# Если нажато 3 из 4 чекбоксов
	elif values[0] == True and values[1] == True and values[2] == True and values[3] == False:
		val = generate_pass(len_pass, az+AZ+spec_sumbol)

	elif values[0] == True and values[1] == True and values[2] == False and values[3] == True:
		val = generate_pass(len_pass, az+AZ+digits)

	elif values[0] == True and values[1] == False and values[2] == True and values[3] == True:
		val = generate_pass(len_pass, az+spec_sumbol+digits)

	elif values[0] == False and values[1] == True and values[2] == True and values[3] == True:
		val = generate_pass(len_pass, AZ+spec_sumbol+digits)

	# Если нажаты все чекбоксы
	elif values[0] == True and values[1] == True and values[2] == True and values[3] == True:
		val = generate_pass(len_pass, az+AZ+spec_sumbol+digits)

	else:
		return 1

	return val