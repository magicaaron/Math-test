import random


def yes_no(question):
    while True:
        user_input = input(question).lower()

        if user_input == "yes" or user_input == "y":
            return "yes"
        elif user_input == "no" or user_input == "n":
            return "no"
        else:
            print("please enter yes or no")


def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', 'x'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        num1, num2 = max(num1, num2), min(num1, num2)
        answer = num1 - num2
    elif operator == 'x':
        answer = num1 * num2

    question = f"What is {num1} {operator} {num2}? "
    return question, answer

#
def take_math_test():
    print("Welcome to my math test.")
    print("You will be asked 6 math questions.")
    print("Let's start.\n")

    score = 0
    num_questions = 6

    for i in range(num_questions):
        question, correct_answer = generate_question()
        print(question)

        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Skip this iteration and move to the next question

        if user_answer == correct_answer:
            print("👍👍 Correct! 👍👍\n")
            score += 1
        else:
            print(f"👎👎 Wrong! 👎👎 The correct answer is {correct_answer}.\n")

    print(f"Test complete! You scored {score} out of {num_questions}.\n")


# Main loop
while True:
    take_math_test()

    play_again = yes_no("Do you want to play again? (yes/no): ")
    if play_again == "yes":
        print()
    elif play_again == "no":
        print ("Thanks for playing!")
        break
