# Birthday Paradox Walkthrough

## 1. What this project is

This project simulates the **birthday paradox**.

The birthday paradox is the surprising idea that in a group of people, the chance that at least two people share the same birthday becomes high much faster than most people expect.

For example, with only 23 people, the chance of a shared birthday is close to 50%. This program does not prove the exact formula mathematically. Instead, it uses repeated random experiments to estimate the probability.

For simplicity, the program uses 365 possible birthdays and does not include leap day.

## 2. What the user experiences

When the user runs the program, they see a short explanation of the birthday paradox. Then the program asks how many birthdays should be generated.

Example interaction:

```text
Birthday Paradox Simulation

The birthday paradox shows that in a group of people, the chance that
at least two people share a birthday is often higher than we expect.

How many birthdays should I generate? (1 to 100)
> 23

Here are 23 randomly generated birthdays:
Jan 5, Mar 14, Jul 21, Jan 5, Nov 9, ...

In this small group, multiple people have a birthday on Jan 5.

Now the program will run 100,000 random simulations.
Press Enter to begin...
```

After the user presses Enter, the program runs many simulations and prints progress updates.

```text
10,000 simulations run...
20,000 simulations run...
30,000 simulations run...
...
100,000 simulations run...
```

Finally, it displays the estimated probability.

```text
Out of 100,000 simulations of 23 people:
- 50,681 groups had at least one matching birthday.
- Estimated probability of a match: 50.68%

That is probably higher than many people expect.
```

The exact birthdays and result will change each time because the program uses random generation.

## 3. Key python concepts used

### Variables

Variables store values the program needs, such as the number of people, generated birthdays, and simulation results.

Example:

```python
people_count = int(response)
```

### Constants

Constants store values that should not change while the program runs.

Example:

```python
MAX_PEOPLE = 100
SIMULATION_COUNT = 100_000
```

These make the code easier to update. For example, if you want to allow 200 people instead of 100, you can change `MAX_PEOPLE` in one place.

### Functions

Functions divide the program into smaller tasks.

For example:

- one function shows the introduction
- one function gets valid input
- one function generates birthdays
- one function checks for a match
- one function runs simulations

This makes the code easier to read and test.

### Loops

Loops are used when the program needs to repeat an action.

Examples:

- keep asking until the user enters valid input
- generate many birthdays
- run 100,000 simulations
- ask whether the user wants to try again

### Conditionals

Conditionals let the program make decisions.

Example:

```python
if matching_birthday is None:
    print("In this small group, there are no matching birthdays.")
else:
    print("In this small group, multiple people have a matching birthday.")
```

### Lists

A list stores all the generated birthdays for one group.

Example:

```python
birthdays = []
```

Each birthday is added to the list as it is created.

### Sets

A set is used to quickly check whether a birthday has already appeared.

Example:

```python
birthdays_seen = set()
```

This is useful because the program only needs to know whether a birthday has appeared before.

### Strings

Strings are used for messages and formatted output.

Example:

```python
return f"{month_name} {birthday.day}"
```

### Input Validation

The program checks that the user enters a whole number between 1 and 100.

This prevents errors and makes the program easier to use.

### Random Module

The `random` module creates random birthdays.

Example:

```python
random_day_offset = random.randint(0, DAYS_IN_YEAR - 1)
```

### Datetime Module

The `datetime` module represents birthdays as real date objects.

Example:

```python
START_OF_YEAR = datetime.date(2001, 1, 1)
```

The year is not important here. The program only cares about the month and day.

### Return Values

Some functions send a result back to the part of the program that called them.

Example:

```python
return round((matching_count / simulation_count) * 100, 2)
```

This returns the estimated probability as a percentage.

## 4. Project workflow

1. The program shows a short introduction.
2. The program asks the user how many birthdays to generate.
3. The program validates the input.
4. The program creates one random group of birthdays.
5. The program displays those birthdays.
6. The program checks whether the small group has a matching birthday.
7. The program tells the user whether a match was found.
8. The user presses Enter to start the larger simulation.
9. The program runs 100,000 random simulations.
10. For each simulation, the program generates a new group of birthdays.
11. For each generated group, the program checks whether at least one birthday is repeated.
12. The program counts how many simulations had a match.
13. The program converts the count into a percentage.
14. The program displays the final probability estimate.
15. The program asks whether the user wants to try another group size.
16. The program either repeats or exits.

## 5. Function-by-function explanation

### `show_intro()`

**What it does:**  
Prints the welcome message and explains the birthday paradox in simple language.

**Input it receives:**  
No input.

**Output it returns:**  
No returned value. It only prints text.

**Why it exists:**  
It keeps the introduction separate from the rest of the program logic.

### `get_number_of_people()`

**What it does:**  
Asks the user how many birthdays to generate.

**Input it receives:**  
User input from the terminal.

**Output it returns:**  
An integer between 1 and 100.

**Why it exists:**  
It handles input validation in one place.

Example:

```text
How many birthdays should I generate? (1 to 100)
> 23
```

The function returns:

```python
23
```

### `generate_birthdays(number_of_birthdays)`

**What it does:**  
Creates a list of random birthday dates.

**Input it receives:**  
The number of birthdays to create.

**Output it returns:**  
A list of `datetime.date` objects.

**Why it exists:**  
The program needs a reusable way to create random birthday groups.

Example:

```python
generate_birthdays(3)
```

Possible result:

```python
[datetime.date(2001, 1, 5), datetime.date(2001, 7, 21), datetime.date(2001, 1, 5)]
```

### `format_birthday(birthday)`

**What it does:**  
Converts a date object into a simple format like `Jan 5`.

**Input it receives:**  
One `datetime.date` object.

**Output it returns:**  
A string.

**Why it exists:**  
Date objects are useful for logic, but formatted strings are easier for users to read.

Example:

```python
format_birthday(datetime.date(2001, 1, 5))
```

Returns:

```python
"Jan 5"
```

### `display_birthdays(birthdays)`

**What it does:**  
Prints the generated birthdays in a comma-separated list.

**Input it receives:**  
A list of birthday date objects.

**Output it returns:**  
No returned value. It prints the birthdays.

**Why it exists:**  
It keeps display logic separate from birthday generation logic.

### `find_matching_birthday(birthdays)`

**What it does:**  
Checks whether any birthday appears more than once.

**Input it receives:**  
A list of birthday date objects.

**Output it returns:**  
The first repeated birthday found, or `None` if there is no match.

**Why it exists:**  
This is the main logic that detects whether the birthday paradox appears in a group.

Example:

```python
birthdays = [
    datetime.date(2001, 1, 5),
    datetime.date(2001, 7, 21),
    datetime.date(2001, 1, 5),
]
```

The function returns:

```python
datetime.date(2001, 1, 5)
```

### `count_matching_simulations(people_count, simulation_count)`

**What it does:**  
Runs many birthday simulations and counts how many groups had at least one matching birthday.

**Input it receives:**

- `people_count`: how many people are in each simulated group
- `simulation_count`: how many simulations to run

**Output it returns:**  
The number of simulations that had a matching birthday.

**Why it exists:**  
This function performs the Monte Carlo simulation.

A Monte Carlo simulation means the program repeats random experiments many times and uses the results to estimate a probability.

### `calculate_probability(matching_count, simulation_count)`

**What it does:**  
Converts the number of matching simulations into a percentage.

**Input it receives:**

- `matching_count`: how many simulations had a match
- `simulation_count`: total number of simulations

**Output it returns:**  
A percentage rounded to 2 decimal places.

**Why it exists:**  
It keeps the probability calculation separate and easy to understand.

Example:

```python
calculate_probability(50681, 100000)
```

Returns:

```python
50.68
```

### `display_simulation_result(people_count, matching_count, simulation_count)`

**What it does:**  
Prints the final simulation result clearly.

**Input it receives:**

- the number of people in each group
- the number of matching simulations
- the total number of simulations

**Output it returns:**  
No returned value. It prints the result.

**Why it exists:**  
It keeps result formatting separate from simulation logic.

### `run_experiment()`

**What it does:**  
Runs one complete experiment from start to finish.

**Input it receives:**  
User input from the terminal.

**Output it returns:**  
No returned value.

**Why it exists:**  
It connects the smaller functions into one complete project flow.

It handles:

- getting the group size
- generating birthdays
- checking the small group
- running the large simulation
- showing the final result

### `ask_to_run_again()`

**What it does:**  
Asks whether the user wants to try another group size.

**Input it receives:**  
User input from the terminal.

**Output it returns:**  
`True` if the user wants to continue, or `False` if the user wants to stop.

**Why it exists:**  
It improves the user experience by allowing replay without restarting the file.

### `main()`

**What it does:**  
Starts the program and controls the main repeat loop.

**Input it receives:**  
No direct input.

**Output it returns:**  
No returned value.

**Why it exists:**  
It gives the program a clear starting point.

The file ends with:

```python
if __name__ == "__main__":
    main()
```

This means the program starts only when the file is run directly.

## 6. Important code snippets

### Snippet 1: Using constants

```python
MIN_PEOPLE = 1
MAX_PEOPLE = 100
DAYS_IN_YEAR = 365
SIMULATION_COUNT = 100_000
PROGRESS_INTERVAL = 10_000
START_OF_YEAR = datetime.date(2001, 1, 1)
```

This stores important settings at the top of the file.

This matters because the code becomes easier to change. For example, a learner can reduce `SIMULATION_COUNT` to `10_000` if they want the program to run faster.

### Snippet 2: Validating user input

```python
if not response.isdecimal():
    print("Please enter a whole number.")
    continue

people_count = int(response)
if MIN_PEOPLE <= people_count <= MAX_PEOPLE:
    return people_count
```

This checks that the user typed a valid whole number.

This matters because user input is unpredictable. Without validation, the program could crash if the user typed text like `hello`.

### Snippet 3: Generating random birthdays

```python
random_day_offset = random.randint(0, DAYS_IN_YEAR - 1)
birthday = START_OF_YEAR + datetime.timedelta(days=random_day_offset)
birthdays.append(birthday)
```

This picks a random number between 0 and 364. Then it adds that many days to January 1.

For example:

- offset `0` means January 1
- offset `30` means January 31
- offset `364` means December 31

This matters because it creates random birthdays in a simple and realistic way.

### Snippet 4: Finding a repeated birthday

```python
birthdays_seen = set()

for birthday in birthdays:
    if birthday in birthdays_seen:
        return birthday
    birthdays_seen.add(birthday)
```

This uses a set to remember birthdays that have already appeared.

If the current birthday is already in the set, the program has found a match.

This matters because it is simple, readable, and efficient.

### Snippet 5: Running many simulations

```python
for simulation_number in range(1, simulation_count + 1):
    birthdays = generate_birthdays(people_count)

    if find_matching_birthday(birthdays) is not None:
        matching_simulations += 1
```

This is the core simulation loop.

Each loop creates a new random group and checks whether that group has a matching birthday.

This matters because the program estimates probability by repeating the same random experiment many times.

### Snippet 6: Calculating probability

```python
return round((matching_count / simulation_count) * 100, 2)
```

This converts the result into a percentage.

For example, if 50,681 out of 100,000 simulations had a match:

```text
50681 / 100000 * 100 = 50.681
```

Rounded to 2 decimal places, this becomes:

```text
50.68%
```

## 7. What this project teaches

This project teaches how Python can be used to understand a surprising real-world probability idea through simulation.

After completing this project, a learner should understand how to:

- break a program into clear functions
- validate user input
- generate random data
- store values in lists and sets
- use loops to repeat experiments
- calculate a simple probability
- present results in a user-friendly way

Most importantly, the learner sees how code can turn an abstract concept into something observable and practical.
