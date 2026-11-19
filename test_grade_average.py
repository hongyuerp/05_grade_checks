import pytest

from grade_average import calculate_average


@pytest.mark.parametrize("first, second, expected", [
    (0, 0, 0),
    (100, 100, 100),
    (0, 100, 50),
    (60, 80, 70),
    (50, 51, 50.5),
])
def test_average_of_valid_marks(first, second, expected):
    assert calculate_average(first, second) == expected


@pytest.mark.parametrize("invalid", [-1, 101])
def test_first_mark_out_of_range(invalid):
    with pytest.raises(ValueError):
        calculate_average(invalid, 50)


@pytest.mark.parametrize("invalid", [-1, 101])
def test_second_mark_out_of_range(invalid):
    with pytest.raises(ValueError):
        calculate_average(50, invalid)


@pytest.mark.parametrize("invalid", [50.0, "50", True, None])
def test_first_mark_has_invalid_type(invalid):
    with pytest.raises(TypeError):
        calculate_average(invalid, 50)


@pytest.mark.parametrize("invalid", [50.0, "50", True, None])
def test_second_mark_has_invalid_type(invalid):
    with pytest.raises(TypeError):
        calculate_average(50, invalid)
