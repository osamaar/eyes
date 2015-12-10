import unittest
from vect2d import Vect2d

class TestVect2d(unittest.TestCase):
    def test_add_vectors(self):
        a = Vect2d(1, 4)
        b = Vect2d(3, 2)
        c = a + b
        self.assertEqual(c.x, 4)
        self.assertEqual(c.y, 6)

    def test_sub_vectors(self):
        a = Vect2d(1, 4)
        b = Vect2d(3, 2)
        c = a - b
        self.assertEqual(c.x, -2)
        self.assertEqual(c.y, 2)

    def test_mul_vectors(self):
        a = Vect2d(1, 4)
        n = 3
        b = a*n
        self.assertEqual(b.x, 3)
        self.assertEqual(b.y, 12)

    def test_mul_vectors_fail(self):
        a = Vect2d(1, 4)
        n = 'a'
        f = lambda: a*n
        self.assertRaises(TypeError, f)
 
    def test_dot_product(self):
        a = Vect2d(1, 4)
        b = Vect2d(3, 2)
        p = a.dot(b)
        self.assertEqual(p, 1*3 + 4*2)

    def test_len(self):
        a = Vect2d(1, 4)
        self.assertEqual(len(a), 2)

    def test_getitem(self):
        a = Vect2d(1, 4)
        self.assertEqual(a[0], 1)
        self.assertEqual(a[1], 4)

    def test_getitem_fails(self):
        a = Vect2d(1, 4)
        self.assertRaises(IndexError, a[2])

    def test_mag(self):
        a = Vect2d(3, 4)
        self.assertEqual(a.mag(), 5)

    def test_unit(self):
        a = Vect2d(0, 3)
        u = a.unit()
        self.assertEqual(u.x, 0)
        self.assertEqual(u.y, 1)

if __name__ == '__main__':
    unittest.main()

