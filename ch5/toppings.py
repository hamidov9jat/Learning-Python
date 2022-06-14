requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

game_active = True
can_edit = False

print(game_active)
print(can_edit)

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 87

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
# else:
#     price = 20

print(f"Your admission cost is ${price}.")

a = [23, 54, 78, 98]

if 23 in a:
    print('yes')

if 89 not in a:
    print("it isn't")



