favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print(f"{name.title()} likes the following numbers:", end = " ")
    for index, number in enumerate(numbers):
        print(f"{number}", end = ", " if (index < len(numbers) - 1) else "\n")