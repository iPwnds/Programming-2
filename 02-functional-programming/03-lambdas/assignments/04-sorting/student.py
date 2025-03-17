def sort_by_age(people):
<<<<<<< HEAD
    return sorted(people, key=lambda person: person.age)

def sort_by_decreasing_age(people):
    return sorted(people, key=lambda person: -person.age)

def sort_by_name(people):
    return sorted(people, key=lambda person: person.name)

def sort_by_name_then_age(people):
    return sorted(people, key=lambda person: (person.name, person.age))

def sort_by_name_then_decreasing_age(people):
    return sorted(people, key=lambda person: (person.name, -person.age))
=======
    # orders the Persons by increasing age.
    return sorted(people, key=lambda people: people.age)

def sort_by_decreasing_age(people):
    # orders the Persons by decreasing age.
    return sorted(people, key=lambda people : -people.age)

def sort_by_name(people):
    # orders the Persons by name, alphabetically.
    return sorted(people, key=lambda people : people.name)

def sort_by_name_then_age(people):
    # orders the Persons by name, and in case of equal names, by increasing age
    return sorted(people, key=lambda people : (people.name, people.age))

def sort_by_name_then_decreasing_age(people):
    # orders the Persons by name, and in case of equal names, by decreasing age
    return sorted(people, key=lambda people : (people.name, -people.age))
>>>>>>> 4c5538f (lambdas done)
