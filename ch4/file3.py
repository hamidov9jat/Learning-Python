players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players, end='\n\n')
print(players[2:])
print(players[:4])
print(players[1:4])
print(players[0:3])

# this prints the last three elements and 
# would continue to work as the list changes in size
print(players[-3:]) # same as print(players[2:])
del players[-1]
print(players)
print(players[-3:]) # still works
print(players[::2])

players[-1:-1] = 'additional'
print(players)
players[len(players):len(players)] = 'hello'
print(players)
players[len(players):len(players)] = ['new value']
print(players)

players[len(players):len(players)] = 'hello'

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title(), end = ', ')
print()




