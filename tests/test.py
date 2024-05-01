from math_package.number import Number


def test_one_plus_one():
    try:
        assert Number(1).plus_one() == 2
    except AssertionError:
        exit(1)


def test_one_plus_two():
    try:
        assert Number(1).plus_one() == 3
    except AssertionError:
        exit(1)
