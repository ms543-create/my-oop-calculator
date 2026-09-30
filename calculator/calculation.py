"""Begin with one concrete object before introducing an abstract parent."""


class Add:
    """Keep the inputs and behavior for one addition together."""

    def __init__(self, a, b):
        # self refers to the new instance. For Add(10, 5), a is 10 and b is 5.
        # Each instance keeps its own operand attributes.
        self.a = a
        self.b = b

    def get_result(self):
        # A method can use the state belonging to the receiving object.
        return self.a + self.b