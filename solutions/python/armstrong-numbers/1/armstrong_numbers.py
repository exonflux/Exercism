def is_armstrong_number(number):
    digits = []
    for char in str(number):
        digits.append(int(char))

    power = len(digits)

    total = 0
    for d in digits:
        total = total + d ** power

    return total == number