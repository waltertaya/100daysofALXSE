import unittest
import operations


class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(operations.add(30, 56), 86)
        self.assertEqual(operations.add(-9, 9), 0)
        self.assertEqual(operations.add(-8, -6), -14)
        self.assertEqual(operations.add(-8, 6), -2)

    def test_subtract(self):
        self.assertEqual(operations.subtract(56, 30), 26)
        self.assertEqual(operations.subtract(9, 9), 0)
        self.assertEqual(operations.subtract(-8, -6), -2)
        self.assertEqual(operations.subtract(-8, 6), -14)
        self.assertEqual(operations.subtract(8, -6), 14)
    
    def test_multiply(self):
        self.assertEqual(operations.multiply(3, 6), 18)
        self.assertEqual(operations.multiply(-4, 9), -36)
        self.assertEqual(operations.multiply(-8, -6), 48)
        self.assertEqual(operations.multiply(0, 6), 0)
    
    def test_divide(self):
        self.assertEqual(operations.divide(3, 6), 0.5)
        self.assertEqual(operations.divide(9, 3), 3)
        self.assertEqual(operations.divide(-8, -4), 2)
        self.assertEqual(operations.divide(0, 6), 0)

        self.assertRaises(ValueError, operations.divide, 7, 0)

        # Using context manager
        with self.assertRaises(ValueError):
            operations.divide(7, 0)



if __name__ == '__main__':
    unittest.main()
