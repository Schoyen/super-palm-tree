class SuperPalmTree:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return (self.a + self.b - self.c) * x

    def unpack(self):
        yield self.a
        yield self.b
        yield self.c
