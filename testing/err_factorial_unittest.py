import unittest

def err_func_factorial(number):
    if number < 0:
        raise ValueError('Factorial is not defined for negative values')
    factorial = 1
    while number > 0:
        factorial = factorial * number
        number = number - 1
    return factorial

class TestFactorial(unittest.TestCase):
    def test_err_func_1(self):
        self.assertEqual(err_func_factorial(3), 6)
    def test_err_func_2(self):
        self.assertEqual(err_func_factorial(4), 24)
