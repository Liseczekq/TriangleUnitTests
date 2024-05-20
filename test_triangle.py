import unittest
from triangle import czy_utworzy_trojkat

class TestTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(czy_utworzy_trojkat(3, 4, 5))
        self.assertTrue(czy_utworzy_trojkat(5, 12, 13))
        self.assertTrue(czy_utworzy_trojkat(7, 10, 5))

    def test_invalid_triangle(self):
        self.assertFalse(czy_utworzy_trojkat(1, 1, 2))
        self.assertFalse(czy_utworzy_trojkat(5, 1, 1))
        self.assertFalse(czy_utworzy_trojkat(0, 0, 0))

    def test_negative_sides(self):
        self.assertFalse(czy_utworzy_trojkat(-1, 2, 3))
        self.assertFalse(czy_utworzy_trojkat(3, -4, 5))
        self.assertFalse(czy_utworzy_trojkat(6, 8, -10))

    def test_zero_sides(self):
        self.assertFalse(czy_utworzy_trojkat(0, 4, 5))
        self.assertFalse(czy_utworzy_trojkat(3, 0, 5))
        self.assertFalse(czy_utworzy_trojkat(3, 4, 0))

if __name__ == '__main__':
    unittest.main()        
