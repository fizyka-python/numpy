# coding: utf-8

import sys
import os
import re

import unittest

import numpy as np

import cwiczenia_numpy as cwiczenia


A = np.array([[ 0, -5,  6, -2, -7,  4],
              [-1,  1, -3,  3,  4,  5],
              [ 8,  6,  8,  1,  8, -2],
              [ 5,  7,  0, -6, -4,  2],
              [-4, -6, -7,  0,  2, -1],
              [-7,  2,  8, -5,  1,  4]], dtype=float)


class TestZastąpZera(unittest.TestCase):
    def setUp(self):
        self.A = A

    def test_zastąp_zera(self):
        res = np.array([[10, -5,  6, -2, -7,  4],
                        [-1,  1, -3,  3,  4,  5],
                        [ 8,  6,  8,  1,  8, -2],
                        [ 5,  7, 10, -6, -4,  2],
                        [-4, -6, -7, 10,  2, -1],
                        [-7,  2,  8, -5,  1,  4]])
        cwiczenia.zastap_zera(self.A, 10)
        np.testing.assert_equal(A, res)


class TestWyśrodkuj(unittest.TestCase):
    def setUp(self):
        self.A = A.copy()

    def test_wyśrodkuj(self):
        res = A - np.average(A.ravel())
        np.testing.assert_allclose(cwiczenia.wysrodkuj(self.A), res)

    def test_A_niezmieniona(self):
        cwiczenia.wysrodkuj(A)
        np.testing.assert_equal(A, self.A)


class TesSumyPoniżej(unittest.TestCase):

    def setUp(self):
        self.A = A.copy()

    def test_sumy_poniżej(self):
        a = A.copy()
        j, i = np.meshgrid(range(a.shape[0]), range(a.shape[1]))
        a[j >= i] = 0.
        np.testing.assert_allclose(cwiczenia.sumy_ponizej(self.A), sum(a, 0))


class TestNaPrzemian(unittest.TestCase):
    def test_nieparzyste(self):
        np.testing.assert_equal(cwiczenia.na_przemian(5),
                                np.array([[ 1.,  0.,  1.,  0.,  1.],
                                          [ 0.,  1.,  0.,  1.,  0.],
                                          [ 1.,  0.,  1.,  0.,  1.],
                                          [ 0.,  1.,  0.,  1.,  0.],
                                          [ 1.,  0.,  1.,  0.,  1.]]))

    def test_parzyste(self):
        np.testing.assert_equal(cwiczenia.na_przemian(4),
                                np.array([[ 1.,  0.,  1.,  0.],
                                          [ 0.,  1.,  0.,  1.],
                                          [ 1.,  0.,  1.,  0.],
                                          [ 0.,  1.,  0.,  1.]]))

if __name__ == '__main__':
    unittest.main()
