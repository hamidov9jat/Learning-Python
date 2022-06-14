def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    if not toppings:
        print(f"Making {size}-inch pizza without any topping")
        return

    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(23)
make_pizza(25, 'mushrooms', 'green peppers', 'extra cheese')
