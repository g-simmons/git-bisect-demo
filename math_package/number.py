class Number:
    def __init__(self, value):
        self.value = value

    def plus_one(self):
        return Number(self.value + 1)

    def plus_two(self):
        return Number(self.value + 2)

    def plus_three(self):
        return Number(self.value + 3)

    def plus_five(self):
        return Number(self.value + 5)

    def plus_seven(self):
        return Number(self.value + 7)

    def plus_four(self):
        return Number(self.value + 4)

    def __eq__(self, other):
        return self.value == other.value
