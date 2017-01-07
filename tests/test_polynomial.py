import pytest

from polynomial import solve_x2, NoRealSolutionException, NotQuadraticEqException


# tests for 'x2_sample'


def test_happy_flow():
    (x1, x2,) = solve_x2(a=1, b=-2, c=1)
    assert (x1, x2,)==(1.0, 1.0,)

def test_no_real_solution():
    with pytest.raises(NoRealSolutionException):
        solve_x2(a=1, b=1, c=1)

def test_linear():
    with pytest.raises(NotQuadraticEqException):
        solve_x2(a=0, b=1, c=-1)

def test_only_a():
    (x1, x2,) = solve_x2(1)
    assert (x1, x2,)==(0.0, 0.0,)

