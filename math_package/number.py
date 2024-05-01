class Number:
    def __init__(self, value):
        self.value = value

    def plus_one(self):
        return Number(self.value + 1)

    def plus_two(self):
        return Number(self.value + 1)

    def plus_three(self):
        return Number(self.value + 2)

    def __eq__(self, other):
        return self.value == other.value
