dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#TypeError: 'tuple' object does not support item assignment
#dimensions[0] = 250

my_t = (3,)
print(my_t)
print(my_t[-1])
print(my_t[0])

for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

my_foods = ('pizza', 'falafel', 'carrot cake', 'fjdsl', 'afgise', 'kaiefe')
#TypeError: 'tuple' object does not support item assignment
#my_foods[2] = 'fhweiuh'
for food in my_foods:
    print(food, end=', ')
print()

my_foods = ('dfjaso', 'afjeawi', 'fjaisew')
for food in my_foods:
    print(food, end=', ')
print()

















