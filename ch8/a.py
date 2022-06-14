# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
#
#
# greet_user()
# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")
#
#
# greet_user('jesse')

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet('willie')
describe_pet(pet_name='willie')