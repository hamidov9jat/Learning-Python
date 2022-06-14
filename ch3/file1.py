bicycles = ['trek', 'cannondale', 'redline', 'specialized', 78, 2.34]
print(bicycles)
print(bicycles[-6])
print(bicycles[5])
print(len(bicycles)) # number of elements in the list above

# return 1st element in the list
print(bicycles[-len(bicycles)]) # bicycles[-6]

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)