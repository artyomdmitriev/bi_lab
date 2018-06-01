import pytasks
import unittest


class TestPytasks(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(pytasks.is_palindrome(1221))

    def test_count_characters(self):
        correct_dict = {'a': 2, 'b': 2, 'c': 1, 'd': 1}
        self.assertEqual(pytasks.count_characters('abcdab'), correct_dict)
        self.assertEqual(pytasks.count_characters(), correct_dict)

    def test_fizzbuzz(self):
        self.assertEqual(pytasks.fizzbuzz(30), 'FizzBuzz')
        self.assertEqual(pytasks.fizzbuzz(9), 'Fizz')
        self.assertEqual(pytasks.fizzbuzz(5), 'Buzz')
        self.assertEqual(pytasks.fizzbuzz(11), 11)


if __name__ == '__main__':
    unittest.main()
