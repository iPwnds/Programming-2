def sort_by_age(people):
    # orders the Persons by increasing age.
    return sorted(people, key=lambda person: person.age)

def sort_by_decreasing_age(people):
    # orders the Persons by decreasing age.
    return sorted(people, key=lambda person: person.age)

def sort_by_name(people):
    # orders the Persons by name, alphabetically.


def sort_by_name_then_age(people):
    # orders the Persons by name, and in case of equal names, by increasing age


def sort_by_name_then_decreasing_age(people):
    # orders the Persons by name, and in case of equal names, by decreasing age