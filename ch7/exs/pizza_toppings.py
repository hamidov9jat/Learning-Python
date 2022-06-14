prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

available_toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage"]

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    elif topping.lower() not in available_toppings:
        print(f"  I'll add {topping} to your pizza.")
    else:
        print("Sorry we don't have such topping")