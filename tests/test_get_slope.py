from unittest import TestCase
from apparatus import get_slope

class TestGet_slope(TestCase):
    def test_get_slope_up(self):
        self.assertEqual(get_slope((1,2,3)),1)

    def test_get_slope_down(self):
        self.assertEqual(get_slope((3,2,1)),-1)

    def test_get_slope_flat(self):
        self.assertEqual(get_slope((1,1,1)),0)

    def test_get_slope_single(self):
        self.assertEqual(get_slope((1,)),0)

    def test_get_slope_null(self):
        self.assertEqual(get_slope(list()),0)
