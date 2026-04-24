
class Add:
    def __init__(self, value):
        self.total = value

    def __call__(self, value):
        return Add(self.total + value)

    def __int__(self):
        return self.total

    def __add__(self, other):
        return self.total + other

    def __radd__(self, other):
        return other + self.total

    def __repr__(self):
        return str(self.total)


def add(x):
    return Add(x)


print(add(1)(2)(3))