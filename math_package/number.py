class Number:
    def __init__(self, value):
        self.value = value

    def plus_one(self):
        return Number(self.value + 1)

    def __eq__(self, other):
        return self.value == other.value
