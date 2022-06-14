names = ['Nijat', 'Elchin', 'Emin', 'Murad']
print(f'{names[0]} or {names[-len(names)]}')

print(f'{names[1]} or {names[-len(names) + 1]}')

print(f'{names[2]} or {names[-len(names) + 2]}')

print(f'{names[3]} or {names[-len(names) + 3]}\n')

message1 = f'Hello {names[0]}'
print(message1)

message2 = f'Hello {names[1]}'
print(message2)

msg3 = f'Hello {names[2]}'
print(msg3)

msg4 = f'Hello {names[3]}'
print(msg4)

car_models = ['bmw', 'mercedes', 'honda', 'porche']
favourite_car_model = f'My favourite car models are {car_models[0].upper()} \
and {car_models[1].upper()}'
print(favourite_car_model)