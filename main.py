import random
saved_numbers = []
number1 = 0
number2 = 0
def number_generator():
    input("Press enter to generate new number: ")
    number1 = (random.randint(1,14))
    number2 = (random.randint(1,14))
    numbers_combined = number1 + (number2 * 0.01)
    if numbers_combined not in saved_numbers:
        print(numbers_combined)
        saved_numbers.append(numbers_combined)
        number_generator()
    elif numbers_combined in saved_numbers:
        number1 = (random.randint(0,14))
        number2 = (random.randint(0,14))
        if numbers_combined not in saved_numbers:
            number_generator()

number_generator()
