for value in range(1, 5):
	print(value, end = ' ')
print('\n')

for value in range(1, 6):
	print(value)
print()

for x in range(8):
	print(x, end = ' ')
print()

numbers = list(range(10))
print(numbers)

even_numbers = list(range(0, 10, 2))
print(even_numbers)

squares = []
print("Squares of the numbers from 1 to 10")
for value in range(1, 11):
	# square = value ** 2
	# squares.append(square)
	squares.append(value**2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)


