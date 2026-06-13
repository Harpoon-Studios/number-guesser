# Number Guesser — Lesson Plan

**Audience:** Friends who have never coded before  
**Time:** ~90 minutes (one session)  
**Goal:** Write and understand a complete Python program from scratch

---

## Session Overview

| Section | Topic | What They'll Learn | Time |
|---------|-------|--------------------|------|
| 0 | Setup | Install Python, run a script | 10 min |
| 1 | Comments & Imports | `#`, `"""docstrings"""`, `import` | 5 min |
| 2 | Constants & Variables | naming, `=` assignment, `ALL_CAPS` convention | 5 min |
| 3 | Functions | `def`, parameters, return values, docstrings | 15 min |
| 4 | Input & Output | `print()`, `input()`, f-strings | 10 min |
| 5 | Conditionals | `if`/`elif`/`else`, comparison operators | 10 min |
| 6 | Loops | `while` loops, `break`, `continue` | 10 min |
| 7 | Error Handling | `try`/`except`, `ValueError` | 5 min |
| 8 | The Main Guard | `if __name__ == "__main__"` | 5 min |
| 9 | Play the Game | Run it, break it, fix it | 10 min |
| 10 | Challenges | Extension exercises | 5+ min |

---

## Section 0: Setup (10 min)

Before the session, each person needs:

1. **Python 3** installed (python.org or `winget install Python.Python.3`)
2. **A text editor** — recommend VS Code, or a simple editor like Notepad++
3. **The project files** — share `number_guesser.py` and `lesson_plan.md`

**Check:** Run `python --version` in the terminal to confirm Python is installed.

---

## Section 1: Comments & Imports (5 min)

Open `number_guesser.py` and look at the very top.

**Key questions to ask:**
- What is a comment? (Lines starting with `#` — Python ignores them.)
- Why do we write comments? (To explain *why*, not *what*.)
- What does `import random` do? (Brings in the random-number generator.)

**Try this:** Delete the `import random` line and run the program. What error do you get? (`NameError: name 'random' is not defined`)

---

## Section 2: Constants & Variables (5 min)

Look at `MIN_NUMBER`, `MAX_NUMBER`, and `MAX_ATTEMPTS`.

**Explain:**
- A **constant** is a value we set once and never change.
- `ALL_CAPS` naming is a convention — Python won't stop you from changing it, but other programmers will know not to.
- Variables store data. `attempts = 0` creates a box labelled "attempts" with the number 0 inside.

**Try this:** Change `MAX_NUMBER` to 1000 and `MAX_ATTEMPTS` to 7. How does the game change?

---

## Section 3: Functions (15 min)

This is the hardest concept for beginners. Go slow.

**Analogy:** A function is like a vending machine.
- You put in money and press a button (the **parameters**).
- The machine does its work (the **body** of the function).
- Out comes a snack (the **return value**).

### `check_guess(guess, secret)` — a function with parameters and a return value

Walk through each line:
```python
def check_guess(guess: int, secret: int) -> str:
```
- `def` = "define a function"
- `check_guess` = the function's name
- `guess: int` = a parameter named `guess` that should be an integer
- `-> str` = this function returns a string

The `if/elif/else` block inside decides what to return.

### `play_round()` — a function with no parameters and no return value

**Ask:** Why is `return` used here? (To exit the function early when the player wins.)

**Try this:** Add a "cheat mode" that prints `secret_number` at the start. (Great way to show they understand variables and scope.)

---

## Section 4: Input & Output (10 min)

### `print()` — showing text

f-strings are your friend:
```python
print(f"Guess #{attempts + 1}: ")
```
The `f` before the string lets you put expressions inside `{curly braces}`.

### `input()` — getting text from the player

`input()` always returns a **string**. Even if the player types `42`, it comes back as `"42"`.

**Try this:** Remove `int()` from the conversion and see what happens when you try to compare `guess < secret_number`. (TypeError.)

---

## Section 5: Conditionals (10 min)

### `if` / `elif` / `else`

Walk through `check_guess`:
1. If guess is less than secret → "too low"
2. Else if guess is greater → "too high"
3. Else (must be equal) → "correct"

### Comparison operators

| Operator | Meaning |
|----------|---------|
| `<` | less than |
| `>` | greater than |
| `==` | equal to |
| `!=` | not equal to |
| `<=` | less than or equal |
| `>=` | greater than or equal |

**Common pitfall:** `=` vs `==`. `=` assigns a value. `==` checks equality.

**Try this:** Change `==` to `=` in `check_guess`. What happens? (SyntaxError.)

---

## Section 6: Loops (10 min)

### `while` loop

```python
while attempts < MAX_ATTEMPTS:
    # keep doing this
```

Think of it like a video game level: you keep playing the level until you either win or run out of lives.

### `continue` — skip the rest and go back to the top

Used when the player enters invalid input. Instead of crashing, we say "try again."

### `break` — exit the loop immediately

Used in the replay loop: `if play_again != "y": break`

**Try this:** Remove the `attempts += 1` line. What happens? (Infinite loop — you'll need to hit Ctrl+C to stop.)

---

## Section 7: Error Handling (5 min)

### `try` / `except`

If the player types "hello" when asked for a number, `int("hello")` raises a `ValueError`. The `try` block "catches" that error and runs the `except` block instead of crashing.

**Try this:** Type "ten" instead of "10" when the game asks for a guess. See how the program handles it gracefully.

---

## Section 8: The Main Guard (5 min)

### `if __name__ == "__main__":`

This checks whether the file is being run directly or imported.

**Demonstration:**
1. Create a new file `test_import.py`:
   ```python
   import number_guesser
   print("Imported successfully!")
   ```
2. Run it. The game should NOT start — only the import happens.

---

## Section 9: Play the Game (10 min)

Let everyone play a few rounds. Encourage them to:
- Try invalid inputs (letters, out-of-range numbers)
- Try to guess in 1 attempt (lucky!)
- Lose on purpose to see the losing message

---

## Section 10: Challenges (extension exercises)

For students who finish early or want homework:

| # | Challenge | Concepts Tested |
|---|-----------|-----------------|
| 1 | Add a "higher/lower" hint that tells the player *how far off* they are (e.g., "very close", "way off") | Conditionals, `abs()` |
| 2 | Add difficulty levels (Easy: 1–50, 10 attempts; Hard: 1–200, 5 attempts) | Nested functions, user choice |
| 3 | Keep a high-score list that persists between runs (save to a file) | File I/O, `open()`, `write()` |
| 4 | Add a two-player mode where Player 1 sets the number and Player 2 guesses | Variable scope, swapping roles |
| 5 | Use `import math` to let the computer give a hint like "the number is a multiple of 7" | Modulo operator, `math` module |

---

## Common Mistakes & How to Fix Them

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `SyntaxError: invalid syntax` | Missing colon (`:`) on `if` or `def` | Add `:` |
| `NameError: name 'X' is not defined` | Typo in variable name | Check spelling |
| `ValueError: invalid literal for int()` | `input()` result not converted | Wrap in `int()` |
| Game runs but nothing happens | `import` line missing | Add `import random` |
| Infinite loop | Missing `attempts += 1` or wrong indentation | Add the counter, check indentation |
| `TypeError: '<' not supported between instances of 'str' and 'int'` | Forgot `int()` conversion | Wrap input in `int()` |

---

## Vocabulary List

| Term | Meaning |
|------|---------|
| **variable** | A named container that holds a value |
| **function** | A reusable block of code |
| **parameter** | An input a function receives |
| **argument** | The actual value passed to a parameter |
| **return value** | The output a function produces |
| **string** | Text data (e.g. `"hello"`) |
| **integer** | Whole number (e.g. `42`) |
| **boolean** | `True` or `False` |
| **loop** | Code that repeats |
| **condition** | An expression that is either True or False |
| **exception** | An error that occurs at runtime |
| **module** | A file containing Python code you can import |

---

## Reference: Running the Game

```bash
# Make sure you're in the project folder
cd path/to/number-guesser

# Run the game
python number_guesser.py
```

On some systems (macOS/Linux), you may need `python3` instead of `python`.
