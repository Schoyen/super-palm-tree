import numpy as np

from super_palm_tree import SuperPalmTree


def test_spt():
    a = 3
    b = 2
    c = 1

    x = np.linspace(-2, 2, 201)

    spt = SuperPalmTree(a, b, c)

    np.testing.assert_allclose((a + b - c) * x, spt(x))

    for (spt_e, e) in zip(spt.unpack(), [a, b, c]):
        assert spt_e == e
