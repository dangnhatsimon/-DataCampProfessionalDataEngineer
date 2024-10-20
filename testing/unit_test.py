import unittest
def func_factorial(number):
    if number < 0:
        raise ValueError('Factorial is not defined for negative values')
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial


class TestFactorial(unittest.TestCase):
    def test_positives(self):
        # Add the test for testing positives here
        self.assertEqual(func_factorial(5), 120)


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        # Add the test for testing zero here
        self.assertEqual(func_factorial(0), 1)


class TestFactorial(unittest.TestCase):
    def test_negatives(self):
      	# Add the test for testing negatives here
        with self.assertRaises(ValueError):
            func_factorial(-1)





def is_prime(num):
    if num == 1: return False
    up_limit = int(math.sqrt(num)) + 1
    for i in range(2, up_limit):
        if num % i == 0:
            return False
    return True

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 17 is prime
        self.assertTrue(is_prime(17), True)

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 6 is not prime
        self.assertFalse(is_prime(6), False)

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 1 is not prime
        self.assertFalse(is_prime(1), False)