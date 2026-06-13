"""
NUMBER GUESSER
A simple Python game where you try to guess a secret number.

This program is designed as a teaching tool for beginners.
Each section introduces a new programming concept.
"""

# ----------------------------------------------------------------------
# LESSON 1: Importing modules
# ----------------------------------------------------------------------
# Python comes with a "standard library" of useful tools.
# The `random` module lets us generate random numbers.
# We use `import` to load it so we can use it in our program.

import random


# ----------------------------------------------------------------------
# LESSON 2: Constants
# ----------------------------------------------------------------------
# A constant is a value that never changes during the game.
# By convention, we write constants in ALL_CAPS so other programmers
# know they shouldn't be modified.

MIN_NUMBER = 1     # The smallest number we might guess
MAX_NUMBER = 100   # The largest number we might guess
MAX_ATTEMPTS = 10  # How many guesses the player gets


# ----------------------------------------------------------------------
# LESSON 3: Defining a function
# ----------------------------------------------------------------------
# A function is a reusable block of code. Think of it like a recipe:
#   - You give it ingredients (parameters / arguments)
#   - It does some steps
#   - It returns a result
#
# This function checks a guess against the secret number and returns
# a hint telling the player whether to guess higher or lower.

def check_guess(guess: int, secret: int) -> str:
    """
    Compare `guess` to `secret` and return a hint.

    Parameters:
        guess  (int): The player's current guess
        secret (int): The number they're trying to find

    Returns:
        str: A hint: "too low", "too high", or "correct"
    """
    if guess < secret:
        return "too low"
    elif guess > secret:
        return "too high"
    else:
        return "correct"


# ----------------------------------------------------------------------
# LESSON 4: Another function — the main game logic
# ----------------------------------------------------------------------
# This function runs a single round of the game.
# It doesn't need any parameters (the parentheses are empty) and
# it doesn't return anything (we just print results to the screen).

def play_round() -> None:
    """
    Play one round of the Number Guesser game.
    """
    # --- LESSON 5: Generating a random number ---
    # randint(a, b) returns a random integer between a and b (inclusive).
    # So random.randint(MIN_NUMBER, MAX_NUMBER) gives us a number
    # between 1 and 100.

    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    # --- LESSON 6: Variables ---
    # A variable stores a value so we can use it later.
    # Here we keep track of how many guesses the player has made.

    attempts = 0

    # --- LESSON 7: The greeting ---
    # f-strings (formatted string literals) let us embed variables
    # or expressions directly inside a string using {curly braces}.

    print(f"\nI'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"Can you guess it in {MAX_ATTEMPTS} tries or fewer?\n")

    # --- LESSON 8: The game loop ---
    # A `while` loop repeats a block of code as long as its condition
    # is True. Here we keep playing until the player runs out of
    # attempts OR guesses correctly.

    while attempts < MAX_ATTEMPTS:

        # --- LESSON 9: Getting input from the user ---
        # input() displays a prompt and waits for the player to type
        # something and press Enter. It always returns a STRING.

        raw_input = input(f"Guess #{attempts + 1}: ")

        # --- LESSON 10: Error handling with try/except ---
        # The player might type something that isn't a number
        # (e.g. "hello"). If we try to convert "hello" to an int,
        # Python will crash with a ValueError.
        # try/except lets us catch that crash gracefully.

        try:
            guess = int(raw_input)  # Convert string → integer
        except ValueError:
            print(f"  Please enter a whole number between {MIN_NUMBER} and {MAX_NUMBER}.\n")
            continue  # Skip the rest of the loop and ask again

        # --- LESSON 11: Range checking ---
        # Make sure the guess is inside the valid range.

        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print(f"  Your guess must be between {MIN_NUMBER} and {MAX_NUMBER}.\n")
            continue

        # --- LESSON 12: Counting attempts ---
        # We only count valid guesses (in-range numbers).
        # `attempts = attempts + 1` can be shortened to `attempts += 1`.

        attempts += 1

        # --- LESSON 13: Checking the guess ---
        # We call our check_guess function and store the result.

        result = check_guess(guess, secret_number)
        print(f"  {guess} is {result}!")

        # --- LESSON 14: Winning condition ---
        # If the result is "correct", the player wins.

        if result == "correct":
            print(f"\nYou got it in {attempts} attempt{'s' if attempts != 1 else ''}!")
            return  # Exit this function early — we're done

        # --- LESSON 15: Remaining attempts ---
        # Let the player know how many tries they have left.

        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"  {remaining} attempt{'s' if remaining != 1 else ''} remaining.\n")

    # --- LESSON 16: Losing condition ---
    # If we exit the while loop without returning, the player lost.

    print(f"\nOut of attempts! The number was {secret_number}.")


# ----------------------------------------------------------------------
# LESSON 17: The "main guard"
# ----------------------------------------------------------------------
# When Python runs a file, it sets the special variable __name__.
#   - If we RUN this file directly, __name__ is "__main__".
#   - If we IMPORT this file from another script, __name__ is
#     "number_guesser" (the module's name).
#
# This if-statement means "only run the game if we execute this file
# directly, not if we import it as a module." It's a standard pattern
# that keeps your code reusable.

if __name__ == "__main__":

    # --- LESSON 18: Program greeting ---

    print("=" * 45)
    print("  Welcome to the Number Guesser!")
    print("=" * 45)

    # --- LESSON 19: The replay loop ---
    # We use a while loop that runs forever (while True) and break
    # out of it when the player doesn't want to play again.

    while True:
        play_round()

        # Ask if they want to play again
        play_again = input("\nPlay again? (y/n): ").strip().lower()

        if play_again != "y":
            print("\nThanks for playing! Goodbye.\n")
            break
