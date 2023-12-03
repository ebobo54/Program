import pytest
from lab_14 import nested_sqrt_recursive, nested_sqrt_non_recursive

@pytest.mark.parametrize("n, expected", [
    (0, 3),
    (1, (3 + 3) ** 0.5),
    (2, ((3 + (3 + 3) ** 0.5)) ** 0.5),
    (3, 2.309635083371176),
])
def test_nested_sqrt_recursive(n, expected):
    assert nested_sqrt_recursive(n) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 3),
    (1, (3 + 3) ** 0.5),
    (2, ((3 + (3 + 3) ** 0.5)) ** 0.5),
    (3, 2.309635083371176),
])
def test_nested_sqrt_non_recursive(n, expected):
    assert nested_sqrt_non_recursive(n) == pytest.approx(expected, abs=1e-5)

if __name__ == "__main__":
    pytest.main()
