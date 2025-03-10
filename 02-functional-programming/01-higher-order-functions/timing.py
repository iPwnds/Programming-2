from time import time
import random

def bubble_sort(unsorted_list):
    """Sorts a list using the bubble sort algorithm."""
    # Create a copy of the argument list
    result_list = list(unsorted_list)
    # A variable to track of whether we made a swap in the last pass
    swapped = True
    while(swapped):
        swapped = False
        for index in range(len(result_list) - 1):
            if result_list[index] > result_list[index + 1]:
                result_list[index], result_list[index + 1] = result_list[index + 1], result_list[index]
                swapped = True
    return result_list

def insertion_sort(unsorted_list):
    """Sorts a list using the insertion sort algorithm."""
    # We move the first item of the unsorted list into the sorted list
    sorted_list = [unsorted_list[0]]
    for element in unsorted_list[1:]:
        inserted = False
        for index, sorted_element in enumerate(sorted_list):
            if sorted_element > element:
                sorted_list.insert(index, element)
                inserted = True
                break
        if not inserted:
            sorted_list.append(element)
    return sorted_list

def test_bubble_sort():
    for size in [1000, 10000]:
        random_list = random.choices(range(0, 101), k=size)
        print(f"Testing performance for list size: {size}")

        start_time = time()
        bubble_sort(random_list)
        end_time = time()
        print(f"Sorting completed in {end_time - start_time} seconds.")
        print()


test_bubble_sort()
