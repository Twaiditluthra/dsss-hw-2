import unittest
from math_quiz import rand_int_generator, rand_arith_generator, calc_result


class TestMathGame(unittest.TestCase):

    def test_rand_int_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rand_arith_generator(self):
        # Test if the result is one of the specified operators
        for _ in range(1000):  # Test a large number of random values
            rand_operator = rand_arith_generator()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_calc_result(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            result = calc_result(num1, num2, operator)
            expected_result = (expected_problem, expected_answer)
            self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

