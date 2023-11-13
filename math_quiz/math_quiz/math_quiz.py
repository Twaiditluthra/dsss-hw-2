import random


def rand_int_generator(min_value, max_value):
    """This shall generate a random integral value in the closed interval of min and a max value."""
    return random.randint(min_value, max_value)


def rand_arith_generator():
    """This shall generate a random arithmetic operator (+, -, *)."""
    return random.choice(['+', '-', '*'])


def calc_result(num1, num2, operator):
    """This shall calculate the result of an arithmetic operation specified by the given operator."""
    expression = f"{num1} {operator} {num2}"
    result = eval(expression)
    return expression, result


def math_quiz():
    """Conducts a math quiz game."""
    score, total_questions = 0, 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(total_questions):
        num1, num2, operator = rand_int_generator(1, 10), rand_int_generator(1, 5), rand_arith_generator()

        problem, answer = calc_result(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Input is invalid. Kindly use a valid integer!")
            user_answer = 0  # Assume wrong answer for invalid input

        if user_answer == answer:
            print("You're Correct! You earned a point.")
            score += 1
        else:
            print(f"You got it wrong.The correct answer is {answer}.")

    print(f"\nGame over! Your final score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()