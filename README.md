# Arithmetic Formatter

This Python script provides a function, `arithmetic_formatter`, designed to visually arrange and solve a list of arithmetic problems, specifically addition and subtraction. The function can optionally display the answers to these problems. It's designed to help in educational environments, such as classrooms or individual study sessions, by neatly organizing problems in a way that's easy to read and understand.

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
from arithmetic_formatter import arithmetic_formatter
```

2. **Call the function with a list of arithmetic problems:**

```python
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
formatted_problems = arithmetic_formatter(problems, show_answers=True)
print(formatted_problems)
```

3. **Output:**

```python
   32      3801      45      123    
+ 698    -    2    + 43    +  49    
-----    ------    ----    -----    
  730      3799      88      172    
```
