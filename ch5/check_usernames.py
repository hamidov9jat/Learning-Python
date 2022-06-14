current_users = ['admin', "fjAIw", "fjaweio", "kjaw", "auIre", "urEwj"]

for user_index in range(len(current_users)):
    current_users[user_index] = current_users[user_index].lower()

print(current_users)

new_users = ["fsjlkj", "fjAwEio", "RWEIfaw", "kjAw", "RUEIvsioi"]

if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"Enter a new username other than {new_user}")
        else:
            print("The username is available")
else:
    print("No new users")


numbers = list(range(1, 10))

for number in numbers:
    if number == 1: print('1st')
    elif number == 2: print('2nd')
    elif number ==3: print('3rd')
    else: print(f"{number}th")







