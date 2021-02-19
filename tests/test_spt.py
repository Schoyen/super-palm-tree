import numpy as np

from super_palm_tree import SuperPalmTree, construct_calc_mat
from super_palm_tree.spt_lib import (
    construct_calc_mat as construct_calc_mat_rust,
)


def test_spt():
    a = 3
    b = 2
    c = 1

    x = np.linspace(-2, 2, 201)

    spt = SuperPalmTree(a, b, c)

    np.testing.assert_allclose((a + b - c) * x, spt(x))

    for (spt_e, e) in zip(spt.unpack(), [a, b, c]):
        assert spt_e == e


def test_calc_mat():
    spts = [
        SuperPalmTree(0, 1, 2),
        SuperPalmTree(1, 2, 3),
        SuperPalmTree(2, 3, 4),
    ]

    c = construct_calc_mat(spts)

    np.testing.assert_allclose(c, c.T)

    spt_params = [[*spt.unpack()] for spt in spts]
    c_2 = construct_calc_mat_rust(spt_params)

    np.testing.assert_allclose(c, c_2)
