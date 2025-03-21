def fizzbuzz():
    number = 1
    while True:
        if number % 3 == 0 and number % 5 == 0:
            yield 'fizzbuzz'
        elif number % 3 == 0:
            yield 'fizz'
        elif number % 5 == 0:
            yield 'buzz'
        else:
            yield str(number)
        number += 1