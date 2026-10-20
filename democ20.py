def factorial(n):
	"""Return the factorial of a non-negative integer n."""
	if n < 0:
		raise ValueError("n must be a non-negative integer")

	result = 1
	for value in range(2, n + 1):
		result *= value
	return result


try:
	number = int(input("Enter a non-negative integer: "))
	print(f"{number}! = {factorial(number)}")
except ValueError as error:
	print(f"Invalid input: {error}")
