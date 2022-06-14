pizzas = ['Margherita ', 'Veggie', 'Meat', 'Hawaiian', 'Buffalo']
friend_pizzas = pizzas[:]

pizzas.append('pepperoni')
friend_pizzas.append('new pizza')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza, end = ', ')

print('\n')

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza, end = ', ')










