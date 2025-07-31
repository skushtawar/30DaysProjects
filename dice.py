import random

def roll_dice(amount: int = 2) -> list[int]:
    """
    Rolls some dice and returns the results as a list.

    :param amount: The amount of dice to roll.
    :return: A list of dice rolls.
    """
    if amount <= 0:
        raise ValueError
        
    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)
        
    return rolls


def main():
    count = 0  # Initialize roll counter
    while True:
        try:
            user_input: str = input('How many dice would you like to roll? ')

            # To exit the game
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                print(f'You rolled the dice {count} time(s).')
                break

            # Try to parse the user_input to int and roll the dice
            print(*roll_dice(int(user_input)), sep=', ')
            count += 1  # Increment count after successful roll

        except ValueError:
            print('(Please enter a valid number)')


if __name__ == '__main__':
    main()
