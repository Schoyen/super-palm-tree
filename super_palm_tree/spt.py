class SuperPalmTree:
    def __init__(self, a: int, b: int, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return (self.a + self.b) * x / self.c

    def unpack(self):
        yield self.a
        yield self.b
        yield self.c

    def param_tuple(self):
        return (self.a, self.b, self.c)
