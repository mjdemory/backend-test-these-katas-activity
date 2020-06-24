import unittest
import katas
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(8, 4), 12)
        self.assertEqual(katas.add(-4, 4), 0)
        self.assertEqual(katas.add(-4, -4), -8)

    def test_multiply(self):
        self.assertEqual(katas.multiply(8, 4), 32 )
        self.assertEqual(katas.multiply(-4, 4), -16)
        self.assertEqual(katas.multiply(-4, -4), 16)

    def test_power(self):
        self.assertEqual(katas.power(4, 3), 64)
        # self.assertEqual(katas.power(-4, 3), -64)
        #self.assertEqual(katas.power(4, -3), 0.015625)
        # self.assertEqual(katas.power(-4, 3), -0.015625)

    def test_factorial(self):
        self.assertEqual(katas.factorial(4), 24)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(9), 21)


if __name__ == '__main__':
    unittest.main()
