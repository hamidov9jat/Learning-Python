my_foods = ['pizza', 'falafel', 'carrot cake', 'fjdsl', 'afgise', 'kaiefe']
for food in my_foods[:3]:
	print(food)
print()

for food in my_foods[2:5]:
	print(food)
print()

for food in my_foods[-3:]:
	print(food)
for food in my_foods:
	print(food)
print()

friend_foods = my_foods[:]

for food in friend_foods:
	print(food)
print()
print(friend_foods)
print(my_foods)
friend_foods[0] = 'boom'
print(my_foods)
print(friend_foods)

friend_foods = my_foods.copy()
print(my_foods)
friend_foods[0] = 'boom'
print(my_foods)
print(friend_foods)

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

friend_foods = my_foods
print(friend_foods)
print(my_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)







