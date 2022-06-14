print(range(1, 21))

for num in range(10):
	print(num, end = ' ')

print()

# for num in range(1, 10**6):
# 	print(num)

numbers = [number for number in range(1, 10**6 + 1)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

for num in range(1, 20, 2):
	print(num, end = ' ')
print()

for num in range(3, 31, 3):
	print(num, end = ' ')
print()

cubes = [value**3 for value in range(1, 11)]
print("\nCubes of numbers from 1 to 10:")
for cube in cubes:
	print(cube, end = ' ')
print()

cubes = []
for value in range(1, 11):
	# cube = value ** 3
	# cubes.append(cube)
	cubes.append(value**3)
	
print(cubes)









