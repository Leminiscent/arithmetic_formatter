# Arithmetic Formatter

This Python script provides a function, `arithmetic_arranger`, designed to visually arrange and solve a list of arithmetic problems, specifically addition and subtraction. The function can optionally display the answers to these problems. It's designed to help in educational environments, such as classrooms or individual study sessions, by neatly organizing problems in a way that's easy to read and understand.

## Features

- Arranges up to 5 arithmetic problems side by side.
- Supports both addition and subtraction operations.
- Checks for various input errors, including:
  - More than 5 problems.
  - Incorrect operators (only `+` and `-` are accepted).
  - Non-digit characters in numbers.
  - Numbers with more than 4 digits.
- Optionally displays the answers below the problems.

## Usage

1. **Import the function into your script:**

```python
from your_script_name import arithmetic_arranger
