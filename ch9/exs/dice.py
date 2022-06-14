from random import randint as rint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number_rolled = rint(1, self.sides)
        msg = f"Rolling a die: {number_rolled}"
        print(msg)
        return number_rolled


if __name__ == '__main__':
    # die = Dice()
    # for roll in range(10):
    #     die.roll_die()
    # Make a 6-sided die, and show the results of 10 rolls.
    d6 = Dice()

    results = []
    for roll_num in range(10):
        result = d6.roll_die()
        results.append(result)
    print("\n10 rolls of a 6-sided die:")
    print(results)

    # Make a 10-sided die, and show the results of 10 rolls.
    d10 = Dice(sides=10)

    results = []
    for roll_num in range(10):
        result = d10.roll_die()
        results.append(result)
    print("\n10 rolls of a 10-sided die:")
    print(results)
