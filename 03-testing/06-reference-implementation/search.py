class Student:
    def __init__(self, id):
        self.id = id

def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None

def binary_search(students, target_id):
    left = 0
    right = len(students) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_id = students[middle].id

        if middle_id == target_id:
            return students[middle]
        elif target_id < middle_id:
            right = middle - 1
        else:
            left = middle + 1
    return None