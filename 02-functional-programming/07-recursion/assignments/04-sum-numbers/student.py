def sum_numbers(number):
    number = abs(number)

    if number == 0:
        return 0

    return number % 10 + sum_numbers(number // 10)