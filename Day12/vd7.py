# Unittest
import unittest

def add(a, b):
    return a + b

def sub(a, b):
    return a - b + 1

class TestCase1(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(2, 3), 5)

    def testSub(self):
        self.assertEqual(sub(5, 2), 3)

if __name__ == '__main__':
    unittest.main()        