import pytest
from search import Student, linear_search, binary_search

@pytest.mark.parametrize('students', [
    [],
    [Student(id) for id in range(0, 10)],  # consecutive IDs
    [Student(id) for id in [1, 3, 5, 7, 10, 20, 50]],  # gaps in IDs
])
@pytest.mark.parametrize('target_id', range(-5, 55))  # test IDs outside range as well
def test_search_algorithms(students, target_id):
    expected = linear_search(students, target_id)
    actual = binary_search(students, target_id)
    assert expected == actual, f"Mismatch for target_id={target_id} in list {[(s.id) for s in students]}"

@pytest.mark.parametrize('students,target_id,expected_id', [
    ([Student(1), Student(2), Student(3)], 1, 1),  # first student
    ([Student(1), Student(2), Student(3)], 3, 3),  # last student
    ([Student(1), Student(2), Student(3)], 2, 2),  # middle student
    ([Student(1), Student(2), Student(3)], 4, None),  # not found
    ([], 1, None),  # empty list
])
def test_edge_cases(students, target_id, expected_id):
    result_linear = linear_search(students, target_id)
    result_binary = binary_search(students, target_id)

    if expected_id is None:
        assert result_linear is None
        assert result_binary is None
    else:
        assert result_linear is not None and result_linear.id == expected_id
        assert result_binary is not None and result_binary.id == expected_id