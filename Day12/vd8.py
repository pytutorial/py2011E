# Kiem tra mat khau:
#  - Do dai >= 6
#  - Chua it nhat 1 chu so
#  - Chua it nhat 1 chu cai

import unittest

def checkPassword(password):
    if len(password) < 6: return False
  
    hasAlpha = False    
    hasDigit = False

    for c in password:
        if c.isalpha():
            hasAlpha = True

        if c.isdigit():
            hasDigit = True

    return hasAlpha and hasDigit

class TestPassword(unittest.TestCase):
    def testFailLessthan6(self):
        self.assertFalse(checkPassword('abc12'))

    def testFailNoDigit(self):
        self.assertFalse(checkPassword('abcdef'))

    def testFailNoAlpha(self):
        self.assertFalse(checkPassword('123456'))

    def testOk1(self):
        self.assertTrue(checkPassword('abcde1'))

    def testOk2(self):
        self.assertTrue(checkPassword('12345a'))

unittest.main()



