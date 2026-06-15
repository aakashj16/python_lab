'''
Bagels

A deductive logic game where the player guesses a secret number
based on clues.
'''

import random

NUM_DIGITS = 3
MAX_GUESSES = 10
DIGITS = '0123456789'

# this function checks whether the game settings are safe before the game starts.
# since the secret numbers cannot repeat digits, the number of digits must be between 1 and 10.
def validate_settings(num_digits: int) -> None:
    '''
    Validate the game settings before the game starts.

    Since the secret number uses unique digits, NUM_DIGITS cannot be 
    greater than 10.
    '''

    if not 1 <= num_digits <= 10:
        raise ValueError('NUM_DIGITS must be between 1 and 10.')

# this function creates the secret number that the player has to guess.
# it randomly selects unique digits and joins them together as a string.    
def generate_secret_number(num_digits: int) -> str:
    '''
    Generate a secret number with unique digits.

    Example: generate_secret_number(3) could return '619'.
    '''

    return ''.join(random.sample(DIGITS, num_digits))

# this function checks whether a value has repeated digits or not.
# it returns True when every digit appears only once.    
def has_unique_digits(value: str) -> bool:
    '''
    Check whether all digits in the value are unique.

    Example: 
        '123' -> True
        '112' -> False
    '''

    return len(set(value)) == len(value)

# this function checks whether the player's guess follows the all game rules.
# a valid guess must have the right length, only digits, and no repeated digits.
def is_valid_guess(guess: str, num_digits: int) -> bool:
    '''
    Check whether the player's guess is valid or not.

    A valid guess:
    - has the correct length
    - contains only digits
    - has no repeated digits
    '''

    return(
        len(guess) == num_digits
        and guess.isdecimal()
        and has_unique_digits(guess)
    )

# this function compares the player's guess with the secret number.
# it returns clues to help the player reason better.
def get_clues(guess: str, secret_number: str) -> str:
    '''
    Return clues for a guess.

    Clues:
    - Fermi: correct digit in the correct position
    - Pico: correct digit in the wrong position
    - Bagels: no correct digits
    '''

    if guess == secret_number:
        return 'You got it!'
    
    clues = []

    for index, digit in enumerate(guess):
        if digit == secret_number[index]:
            clues.append('Fermi')
        elif digit in secret_number:
            clues.append('Pico')

    if not clues:
        return 'Bagels'
    
    clues.sort()
    return ' '.join(clues)

# this function prints the game instructions for the player.
# it explains the goal of the game, the number of guesses, and the meaning of each clue. 
def display_instructions(num_digits: int, max_guesses: int) -> None:
    '''
    Display the rules of the game.
    '''

    print(f'''
Bagels, a deductive logic game.
          
I'm thinking of a {num_digits}-digit number with no repeated digits.
You have {max_guesses} guesses to find it.

Clues:
- Pico: One digit is correct but in the wrong position.
- Fermi: One digit is correct and in the right position.
- Bagels: No digit is correct.

Example:
    Secret number: 248
    Your guess: 843
    Clue: Fermi Pico
''')

# this function repeatedly asks the player for input until the guess is valid.
# it also allows the player to quit if they want to quit during the current round.    
def get_player_guess(guess_number: int, num_digits: int) -> str:
    '''
    Ask the player for a valid guess.

    The player can type 'q' to quit.
    '''

    while True:
        print(f'Guess #{guess_number}:')
        guess = input('> ').strip()

        if guess.lower() == 'q':
            return 'q'
    
        if is_valid_guess(guess, num_digits):
            return guess
        
        print(
            f'Invalid guess. Please enter a {num_digits}-digit number ' 
              'with no repeated digits.'
        )

# this function controls one complete round of the game.
# it creates the secret number, collects guesses, gives clues, and decides win or loss.
def play_round(num_digits: int, max_guesses: int) -> bool:
    '''
    Play one round of Bagels.

    Returns:
        True if the player wins.
        False if the player loses or quits.
    '''

    secret_number = generate_secret_number(num_digits)

    print('I have thought up a number.')
    print(f'You have {max_guesses} guesses to get it.')
    print('Type "q" anytime to quit the round.')

    for guess_number in range(1, max_guesses + 1):
        guess = get_player_guess(guess_number, num_digits)

        if guess == 'q':
            print('Round ended')
            return False
        
        clues = get_clues(guess, secret_number)
        print(clues)

        if guess == secret_number:
            return True
        
    print('You ran out of guesses.')
    print(f'The answer was {secret_number}')
    return False

# this function asks whether the player wants another round.
# it returns True for answers starting with 'y', such as 'yes' or 'y'.
def ask_to_play_again() -> bool:
    '''
    Ask the player whether they want to play again.
    '''

    answer = input('Do you want to play again? (yes or no): ')
    return answer.lower().startswith('y')

# this is the main entry point of the program.
# it starts the game, tracks wins and losses, and stops when the player chooses not to continue.
def main() -> None:
    '''
    Run the Bagels game.
    '''
    validate_settings(NUM_DIGITS)
    display_instructions(NUM_DIGITS, MAX_GUESSES)

    wins = 0
    losses = 0

    while True:
        player_won = play_round(NUM_DIGITS, MAX_GUESSES)

        if player_won:
            wins = wins + 1

        else:
            losses = losses + 1

        print(f'Score: {wins} wins, {losses} losses')

        if not ask_to_play_again():
            break
    print('Thanks for playing!')

if __name__ == '__main__':
    main()