from math_package.number import Number


def test_one_plus_one():
    try:
        assert Number(1).plus_one() == Number(2)
    except AssertionError:
        exit(1)


def test_two_plus_one():
    try:
        assert Number(2).plus_one() == Number(3)
    except AssertionError:
        exit(1)


def test_one_plus_three():
    try:
        assert Number(1).plus_three() == Number(4)
    except AssertionError:
        exit(1)


if __name__ == "__main__":
    test_one_plus_one()
    test_two_plus_one()
    test_one_plus_three()
    print("All tests passed")
