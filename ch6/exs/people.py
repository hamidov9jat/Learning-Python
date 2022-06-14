# people = [{
#     'first_name': 'eric',
#     'last_name': 'matthes',
#     'age': 43,
#     'city': 'sitka',
#     }, {
#     'first_name': 'nika',
#     'last_name': 'hamidov',
#     'age': 19,
#     'city': 'baku',
#     }, {
#     'first_name': 'kuku',
#     'last_name': 'bird',
#     'age': 5,
#     'city': 'paris',
#     }
# ]

# for person in people:
#     for user_info, value in person.items():
#         if not isinstance(value, int):
#             print(f"{user_info.title()}: {value.title()}")
#         else:
#             print(f"{user_info.title()}: {value}")
#     print()
    
# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'lemmy',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 11,
    'city': 'sitka',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"{name}, of {city}, is {age} years old.")


