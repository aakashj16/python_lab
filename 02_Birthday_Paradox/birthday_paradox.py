'''
Birthday Paradox Simulation

This program explores the birthday paradox with random simulations.

The birthday paradox shows that even a small group of people can have a 
surprisingly high chance of at least two people sharing the same birthday.
'''

import datetime
import random

MIN_PEOPLE = 1
MAX_PEOPLE = 100
DAYS_IN_YEAR = 365
SIMULATION_COUNT = 100_000
PROGRESS_INTERVAL = 10_000
START_OF_YEAR = datetime.date(2001, 1, 1)

MONTH_NAMES = (
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
)

# this function shows the welcome message and explains the purpose of the program
def show_intro() -> None:
    print('''
Birthday Paradox Simulation
          
The birthday paradox shows that in a group of people, the chance that 
at least two people share a birthday is often higher than we expect.
          
This program uses random simulations to estimate that chance.
For simplicity, it uses 365 possible birthdays and does not include leap day.
''')
    
# this function asks the user for the group size and keeps asking until the input is valid
def get_number_of_people() -> int:
    while True:
        print(f'How many birthdays should I generate? ({MIN_PEOPLE} to {MAX_PEOPLE})')
        response = input('> ').strip()

        if not response.isdecimal():
            print('Please enter a whole number.')
            continue

        people_count = int(response)
        if MIN_PEOPLE <= people_count <= MAX_PEOPLE:
            return people_count
        
        print(f'Please enter a number from {MIN_PEOPLE} to {MAX_PEOPLE}')

# this function creates a list of random birthdays for the number of people requested.
def generate_birthdays(number_of_birthdays: int) -> list[datetime.date]:
    birthdays: list[datetime.date] = []

    for _ in range(number_of_birthdays):
        random_day_offset = random.randint(0, DAYS_IN_YEAR - 1)
        birthday = START_OF_YEAR + datetime.timedelta(days = random_day_offset)
        birthdays.append(birthday)

    return birthdays
    
# this function converts a date object into a simple birthday format like 'Aug 10'
def format_birthday(birthday: datetime.date) -> str:
    month_name = MONTH_NAMES[birthday.month - 1]
    return f'{month_name} {birthday.day}'

# this function prints the generated birthdays in a clean comma-separated format
def display_birthdays(birthdays: list[datetime.date]) -> None:
    formatted_birthdays = []

    for birthday in birthdays:
        formatted_birthdays.append(format_birthday(birthday))

    print(', '.join(formatted_birthdays))

# this function looks through the birthday list and returns the first repeated birthday
def find_matching_birthday(birthdays: list[datetime.date]) -> datetime.date | None:
    birthdays_seen = set()

    for birthday in birthdays:
        if birthday in birthdays_seen:
            return birthday
        birthdays_seen.add(birthday)
        
    return None

# this function runs many random birthday groups and counts how many groups had a match.
def count_matching_simulations(people_count: int, simulation_count: int) -> int:
    matching_simulations = 0

    for simulation_number in range(1, simulation_count + 1):
        birthdays = generate_birthdays(people_count)

        if find_matching_birthday(birthdays) is not None:
            matching_simulations = matching_simulations + 1

        if simulation_number % PROGRESS_INTERVAL == 0:
            print(f'{simulation_number:,} simulations run...')

    return matching_simulations

# this function converts the number of successful simulations into a percentage
def calculate_probability(matching_count: int, simulation_count: int) -> float:
    return round((matching_count / simulation_count) * 100, 2)

# this function shows the final result in a simple, readable way
def display_simulation_result(
        people_count: int,
        matching_count: int,
        simulation_count: int
)-> None:
    
    probability = calculate_probability(matching_count, simulation_count)

    print()
    print(f'Out of {simulation_count:,} simulations of {people_count} people:')
    print(f'- {matching_count:,} groups had at least one matching birthday.')
    print(f'- Estimated probability of a match: {probability}%')
    print()
    print('That is probably higher than many people expect.')

# this function runs one complete birthday paradox experiment from input to final result
def run_experiment() -> None:
    people_count = get_number_of_people()
    print()

    birthdays = generate_birthdays(people_count)
    print(f'Here are {people_count} randomly generated birthdays:')
    display_birthdays(birthdays)
    print()

    matching_birthday = find_matching_birthday(birthdays)
    if matching_birthday is None:
        print('In this small group, there are no matching birthdays.')
    else:
        print(
            'In this small group, multiple people have a birthday on '
            f'{format_birthday(matching_birthday)}'
        )

    print()
    print(f'Now the program will run {SIMULATION_COUNT:,} random simulations.')
    input('Press Enter to begin...')
    print()

    matching_count = count_matching_simulations(people_count, SIMULATION_COUNT)
    display_simulation_result(people_count, matching_count, SIMULATION_COUNT)

# this function asks the user whether they want to try another group size
def ask_to_run_again() -> bool:
    while True:
        print()
        response = input('Try another group size? (yes or no)\n> ').strip().lower()

        if response in ('yes', 'y'):
            return True
        if response in ('no', 'n'):
            return False
        
        print('Please enter yes or no.')

# this function starts the program and controls whether the user repeats the experiment
def main() -> None:
    show_intro()

    while True:
        run_experiment()

        if not ask_to_run_again():
            print('Thank you for exploring the birthday paradox.')
            break

if __name__ == '__main__':
    main()