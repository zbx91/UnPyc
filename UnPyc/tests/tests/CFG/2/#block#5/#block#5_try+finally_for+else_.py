for i in range(3):
	try:
		raise NameError('YourNameIncorrect')
	finally:
		raise NameError('YourNameIncorrect')
else:
	try:
		raise NameError('YourNameIncorrect')
	finally:
		raise NameError('YourNameIncorrect')
