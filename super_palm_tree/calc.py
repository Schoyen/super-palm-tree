import numpy as np

from super_palm_tree.spt import SuperPalmTree


def calc_spt(spt_i: SuperPalmTree, spt_j: SuperPalmTree) -> float:
    val = 0

    for attr_i, attr_j in zip(spt_i.unpack(), spt_j.unpack()):
        val += attr_i * attr_j

    return val


def calc_param_spt(spt_i: SuperPalmTree, spt_j: SuperPalmTree) -> float:
    return ((spt_i.a - spt_j.a) + (spt_i.b - spt_j.b)) / (spt_i.c + spt_j.c)


def construct_calc_mat(spts: list) -> np.ndarray:
    l = len(spts)

    c = np.zeros((l, l))

    for i in range(l):
        for j in range(l):
            c[i, j] = calc_spt(spts[i], spts[j])

    return c


def construct_param_mat(spts: list) -> np.ndarray:
    l = len(spts)

    p = np.zeros((l, l))

    for i in range(l):
        for j in range(l):
            p[i, j] = calc_param_spt(spts[i], spts[j])

    return p
