import unittest

from my_sum import my_sum

class MySumTests(unittest.TestCase):

    # def setUp(self):
    #     # setting up
    #     self.numbers = [10, 5, 7, 8, 90, 60]

    def test_sum_of_numbers(self):
        '''
        Test sum of digits/numbers
        '''
        self.assertEqual(my_sum(10, 15), 25)
        self.assertEqual(my_sum(9, 6), 15)
        self.assertEqual(my_sum(9, 9), 18)
        self.assertEqual(my_sum(19,6), 25)
        self.assertEqual(my_sum(91,6), 97)
        self.assertEqual(my_sum(9,6), 15)

    def test_non_numbers(self):
        '''
        Assert throwing of exception when it's a
        a non-number
        '''
        with self.assertRaises(TypeError):
        	my_sum('2',4)
        with self.assertRaises(TypeError):
        	my_sum(7, '9')
        with self.assertRaises(TypeError):
        	 my_sum(5, 'b')

if __name__ == '__main__':
    unittest.main()














