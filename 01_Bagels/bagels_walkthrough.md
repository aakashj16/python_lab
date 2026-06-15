# Bagels Walkthrough

## 1. What this project is

Bagels is a small deductive logic game written in Python.

The computer secretly creates a number with no repeated digits. The player keeps guessing the number. After each guess, the computer gives clues that help the player reason their way to the answer.

## 2. Game rules in simple words

In this version of Bagels:

```python
NUM_DIGITS = 3
MAX_GUESSES = 10
DIGITS = '0123456789'
```

This means:

- The secret number has 3 digits.
- The player gets 10 guesses.
- The secret number is made from digits 0 to 9.
- No digit repeats in the secret number.

## 3. Meaning of the clues

After each guess, the player receives one or more clues.

| Clue | Meaning | Example |
|---|---|---|
| Fermi | Correct digit in the correct position | Secret: `248`, Guess: `243`, digit `2` and `4` are correctly placed |
| Pico | Correct digit but in the wrong position | Secret: `248`, Guess: `843`, digit `8` is present but not in the same position |
| Bagels | No digit is correct | Secret: `248`, Guess: `915` |

## 4. Overall workflow

The project follows this flow:

```text
Start program
    ↓
Validate settings
    ↓
Display instructions
    ↓
Start a round
    ↓
Generate secret number
    ↓
Ask player for a guess
    ↓
Validate the guess
    ↓
Compare guess with secret number
    ↓
Show clues
    ↓
Check win, loss, quit, or next guess
    ↓
Update score
    ↓
Ask whether to play again
    ↓
End program
```

## 5. Constants used in the project

At the top of the file, the game settings are stored as constants:

```python
NUM_DIGITS = 3
MAX_GUESSES = 10
DIGITS = '0123456789'
```

These values control the game.

For example, changing this:

```python
NUM_DIGITS = 4
```

will turn the game into a 4-digit guessing game.

## 6. Function-by-function explanation

## 6.1 `validate_settings()`

This function checks whether the game settings are valid before the game starts.

```python
def validate_settings(num_digits: int) -> None:
    if not 1 <= num_digits <= 10:
        raise ValueError('NUM_DIGITS must be between 1 and 10.')
```

Why this is needed:

The game uses unique digits only. Since digits are from `0` to `9`, there are only 10 possible unique digits.

So this is valid:

```python
NUM_DIGITS = 3
```

But this is not valid:

```python
NUM_DIGITS = 12
```

There are not 12 unique digits available from `0` to `9`.

## 6.2 `generate_secret_number()`

This function creates the secret number.

```python
def generate_secret_number(num_digits: int) -> str:
    return ''.join(random.sample(DIGITS, num_digits))
```

Important part:

```python
random.sample(DIGITS, num_digits)
```

This randomly picks unique digits.

Example:

```python
random.sample('0123456789', 3)
```

could return:

```python
['6', '1', '9']
```

Then this part joins the list into one string:

```python
''.join(['6', '1', '9'])
```

Result:

```python
'619'
```

The secret number is stored as a string, not an integer. This is helpful because a secret number like `047` should keep the starting zero.

## 6.3 `has_unique_digits()`

This function checks whether a value has repeated digits.

```python
def has_unique_digits(value: str) -> bool:
    return len(set(value)) == len(value)
```

The idea is simple:

- `set(value)` removes duplicates.
- If the length stays the same, all digits were unique.
- If the length becomes smaller, something was repeated.

Example 1:

```python
value = '123'
set(value)  # {'1', '2', '3'}
```

Length of original value:

```python
3
```

Length after converting to set:

```python
3
```

So the result is:

```python
True
```

## 6.4 `is_valid_guess()`

This function checks whether the player's guess is acceptable.

```python
def is_valid_guess(guess: str, num_digits: int) -> bool:
    return (
        len(guess) == num_digits
        and guess.isdecimal()
        and has_unique_digits(guess)
    )
```

A valid guess must pass three checks.

| Check | Example that passes | Example that fails |
|---|---|---|
| Correct length | `123` | `12` |
| Only digits | `123` | `12a` |
| No repeated digits | `123` | `112` |

Example:

```python
is_valid_guess('123', 3)
```

Result:

```python
True
```

## 6.5 `get_clues()`

This is the core logic of the game.

It compares the player's guess with the secret number and returns the clue.

```python
def get_clues(guess: str, secret_number: str) -> str:
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
```

### Example 1: Exact match

```text
Secret number: 248
Guess:         248
```

The function returns:

```text
You got it!
```

### Example 2: Some correct digits

```text
Secret number: 248
Guess:         843
```

Step-by-step:

| Guess digit | Position | What happens | Clue |
|---|---:|---|---|
| `8` | 0 | Exists in secret but wrong position | Pico |
| `4` | 1 | Correct digit and correct position | Fermi |
| `3` | 2 | Not in secret | No clue |

The clues list becomes:

```python
['Pico', 'Fermi']
```

Then the clues are sorted:

```python
['Fermi', 'Pico']
```

Final result:

```text
Fermi Pico
```

### Example 3: No correct digits

```text
Secret number: 248
Guess:         915
```

No digits match, so the function returns:

```text
Bagels
```

## 6.6 `display_instructions()`

This function prints the game instructions.

```python
def display_instructions(num_digits: int, max_guesses: int) -> None:
    print(f'''
Bagels, a deductive logic game.
          
I'm thinking of a {num_digits}-digit number with no repeated digits.
You have {max_guesses} guesses to find it.
...
''')
```

This function does not calculate anything. Its job is to make the game easier for the player to understand.

It uses an f-string so that the instructions automatically show the current game settings.

Example:

```python
num_digits = 3
max_guesses = 10
```

The player sees:

```text
I'm thinking of a 3-digit number with no repeated digits.
You have 10 guesses to find it.
```

## 6.7 `get_player_guess()`

This function asks the player for a guess.

```python
def get_player_guess(guess_number: int, num_digits: int) -> str:
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
```

The `while True` loop keeps asking until the player enters either:

- a valid guess, or
- `q` to quit

Example flow:

```text
Guess #1:
> 112
Invalid guess. Please enter a 3-digit number with no repeated digits.

Guess #1:
> 123
```

Now `123` is accepted and returned.

## 6.8 `play_round()`

This function controls one full round of the game.

```python
def play_round(num_digits: int, max_guesses: int) -> bool:
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
```

The function returns a boolean value:

```text
True  -> player won
False -> player lost or quit
```

Example win flow:

```text
Secret number: 248
Guess #1: 123 -> Pico
Guess #2: 843 -> Fermi Pico
Guess #3: 248 -> You got it!
```

The function returns:

```python
True
```

Example loss flow:

```text
The player uses all 10 guesses and does not find the number.
```

The function returns:

```python
False
```

## 6.9 `ask_to_play_again()`

This function asks the player if they want to play another round.

```python
def ask_to_play_again() -> bool:
    answer = input('Do you want to play again? (yes or no): ')
    return answer.lower().startswith('y')
```

## 6.10 `main()`

This is the main function of the program.

```python
def main() -> None:
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
```

This function does four important things:

1. Validates settings.
2. Shows instructions.
3. Runs one or more rounds.
4. Tracks the player's score.

## 7. Why `if __name__ == '__main__'` is used

At the bottom of the file, we have:

```python
if __name__ == '__main__':
    main()
```

This means:

- Run the game only when this file is executed directly.
- Do not automatically run the game if this file is imported into another file.

Example:

```bash
python bagels.py
```

This starts the game.

But if another file imports this file:

```python
import bagels
```

The game will not automatically start.

This is a good professional habit because it makes the code easier to test and reuse.

## Final mental model

Think of the project as three layers.

| Layer | What it does | Functions |
|---|---|---|
| Setup layer | Validates settings and explains rules | `validate_settings()`, `display_instructions()` |
| Logic layer | Generates number, validates guess, creates clues | `generate_secret_number()`, `has_unique_digits()`, `is_valid_guess()`, `get_clues()` |
| Game-flow layer | Runs rounds, tracks score, asks to replay | `get_player_guess()`, `play_round()`, `ask_to_play_again()`, `main()` |

This is a strong structure for a beginner project because each function has a clear responsibility.
