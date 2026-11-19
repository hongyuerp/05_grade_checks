import pytest

from grade_pass import has_passed


@pytest.mark.parametrize("score, expected", [
    (0, False),
    (49, False),
    (50, True),
    (51, True),
    (100, True),
])
def test_pass_status_for_valid_score(score, expected):
    assert has_passed(score) is expected


@pytest.mark.parametrize("score", [-1, 101])
def test_score_out_of_range(score):
    with pytest.raises(ValueError):
        has_passed(score)


@pytest.mark.parametrize("score", [50.0, "50", True, None])
def test_score_has_invalid_type(score):
    with pytest.raises(TypeError):
        has_passed(score)
