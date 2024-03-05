def arithmetic_formatter(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    answers_line = ""

    for problem in problems:
        parts = problem.split()
        first_number = parts[0]
        operator = parts[1]
        second_number = parts[2]

        # Check for valid operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if numbers are valid
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."

        # Check number length
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate space and dashes
        length = max(len(first_number), len(second_number)) + 2
        top = first_number.rjust(length)
        bottom = operator + second_number.rjust(length - 1)
        dash = "-" * length
        if show_answers:
            if operator == "+":
                answer = str(int(first_number) + int(second_number))
            else:
                answer = str(int(first_number) - int(second_number))
            answer = answer.rjust(length)
        else:
            answer = ""

        if problem != problems[-1]:  # If not the last problem, add four spaces
            first_line += top + "    "
            second_line += bottom + "    "
            dashes += dash + "    "
            answers_line += answer + "    "
        else:  # If the last problem, don't add spaces after
            first_line += top
            second_line += bottom
            dashes += dash
            answers_line += answer

    if show_answers:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes}\n{answers_line}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes}"

    return arranged_problems


def main():
    print(f'\n{arithmetic_formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')


if __name__ == "__main__":
    main()
