import pytest
from lab_7 import intersect_recursive, intersect_non_recursive

@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 3, 4], [2, 3, 4, 6, 8], [2, 3, 4]),
    ([5, 8, 2], [2, 9, 1], [2]),
    ([5, 8, 2], [7, 4], []),
])
def test_intersect_recursive(list1, list2, expected):
    assert intersect_recursive(list1, list2) == expected

@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 3, 4], [2, 3, 4, 6, 8], [2, 3, 4]),
    ([5, 8, 2], [2, 9, 1], [2]),
    ([5, 8, 2], [7, 4], []),
])
def test_intersect_non_recursive(list1, list2, expected):
    assert intersect_non_recursive(list1, list2) == expected

if __name__ == "__main__":
    pytest.main()
