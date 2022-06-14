motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(str(motorcycles) + "\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati') # insert the value 'ducati' at the
								# begginig of the list (at index 0)
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles) # ['yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles) # ['yamaha']

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1] # here it will delete 'yamaha' not 'suzuki'
print(motorcycles)
print()

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.insert(0, popped_motorcycle)
print(motorcycles) # ['suzuki', 'honda', 'yamaha']

motorcycles.pop() # 'yamaha' is popped off the top of the stack and returned
				  #  but wasn't used that's why we no longer can access it
				  #  same as del motorcycles[-1]

print(motorcycles)

motorcycles.append(popped_motorcycle)

print(motorcycles)
print(motorcycles.pop(1)) # pop the second motorcycle in the list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
removed = motorcycles.remove(too_expensive)
print(removed) # returns None
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#Bitwise operations only make sense for integers. 
#The result of bitwise operations is calculated as 
#though carried out in two’s complement with an infinite 
#number of sign bits.

x=13
print(x<<2) 
print(x>>2)
print(x) # x is not changed

x = -13
print(x<<2)
print(x>>2)

x=3
print(x<<2) 
print(x>>2)
print()

x=-3
print(x<<2) 
print(x>>2)




