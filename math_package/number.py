class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other)

    def __mul__(self, other):
        return Number(self.value * other)

    def plus_one(self):
        return self + 3

    def plus_two(self):
        return self + 3

    def plus_three(self):
        return self + 3

    def plus_five(self):
        return self + 5

    def plus_seven(self):
        return self + 7

    def plus_four(self):
        return self + 4

    def plus_six(self):
        return self + 6

    def __eq__(self, other):
        return self.value == other.value

    def times_two(self):
        return self * 2
