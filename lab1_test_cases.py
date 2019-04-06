import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_none(self):
        """test case for when int_list in None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_empty_list(self):
        """test case for when int_list is empty"""
        self.assertEqual(max_list_iter([]), None)

    def test_max_list_iter_first_max(self):
        """test case for when first index is max"""
        self.assertEqual(max_list_iter([5, 4, 3]), 5)
        self.assertEqual(max_list_iter([-1, -24, -34]), -1)
        self.assertAlmostEqual(max_list_iter([8.9, 2.3, -0.5]), 8.9)

    def test_max_list_iter_second_max(self):
        """test case for when second index is max"""
        self.assertEqual(max_list_iter([2, 4, 1]), 4)
        self.assertEqual(max_list_iter([-89, -24, -100]), -24)
        self.assertAlmostEqual(max_list_iter([-8, 2.3, -0.5]), 2.3)

    def test_max_list_iter_third_max(self):
        """test case for when third index is max"""
        self.assertEqual(max_list_iter([1, 2, 3]), 3)
        self.assertEqual(max_list_iter([-100, -94, -34]), -34)
        self.assertAlmostEqual(max_list_iter([-8.9, -8, -0.5]), -0.5)

    def test_max_list_iter_all_max(self):
        """test case for when all numbers are max"""
        self.assertEqual(max_list_iter([5, 5, 5]), 5)
        self.assertEqual(max_list_iter([-1, -1, -1]), -1)
        self.assertAlmostEqual(max_list_iter([8.9, 8.9, 8.9]), 8.9)

    def test_max_list_iter_first_two_max(self):
        """test case for when first two nums are max"""
        self.assertEqual(max_list_iter([5, 5, 3]), 5)
        self.assertEqual(max_list_iter([-1, -24, -34]), -1)
        self.assertAlmostEqual(max_list_iter([8.9, 2.3, -0.5]), 8.9)

    def test_max_list_iter_last_two_max(self):
        """test case for when last two nums are max"""
        self.assertEqual(max_list_iter([1, 3, 3]), 3)
        self.assertEqual(max_list_iter([-100, -34, -34]), -34)
        self.assertAlmostEqual(max_list_iter([-8.9, -0.5, -0.5]), -0.5)

    def test_max_list_iter_first_and_third_max(self):
        """test case for when first and third nums are max"""
        self.assertEqual(max_list_iter([3, 2, 3]), 3)
        self.assertEqual(max_list_iter([-34, -94, -34]), -34)
        self.assertAlmostEqual(max_list_iter([-0.5, -8, -0.5]), -0.5)



    def test_reverse_rec_empty_list(self):
        """test case for when int_list is empty"""
        self.assertEqual(reverse_rec([]), [])  # in case of empty lists

    def test_reverse_rec_none(self):
        """test case for when int_list is None""" 
        tlist = None
        with self.assertRaises(ValueError):    # used to check for exception
           reverse_rec(tlist)

    def test_reverse_rec(self):
        """test case for reverse_rec"""
        self.assertEqual(reverse_rec([3, 2, 1]), [1, 2, 3])
        self.assertEqual(reverse_rec([4.5, 2.3, 4]), [4, 2.3, 4.5])
        self.assertEqual(reverse_rec([3, -5, 4.5, 2, 3]), [3, 2, 4.5, -5, 3])

    def test_reverse_rec_all_nums_same(self):
        """test case for when all values are the same"""
        self.assertEqual(reverse_rec([3, 3, 3]), [3, 3, 3])
        self.assertEqual(reverse_rec([4.5, 4.5, 4.5]), [4.5, 4.5, 4.5])
        self.assertEqual(reverse_rec([-5, -5, -5, -5]), [-5, -5, -5, -5])

    def test_reverse_rec_first_two_nums_same(self):
        """test case for when first two values are the same"""
        self.assertEqual(reverse_rec([3, 3, 1]), [1, 3, 3])
        self.assertEqual(reverse_rec([4.5, 4.5, 6.5]), [6.5, 4.5, 4.5])
        self.assertEqual(reverse_rec([-5, -5, -3]), [-3, -5, -5])

    def test_reverse_rec_last_two_nums_same(self):
        """test case for when last two values are the same"""
        self.assertEqual(reverse_rec([3, 3, 3]), [3, 3, 3])
        self.assertEqual(reverse_rec([4.5, 4.5, 4.5]), [4.5, 4.5, 4.5])
        self.assertEqual(reverse_rec([-5, -5, -5, -5]), [-5, -5, -5, -5])

    def test_reverse_rec_first_and_last_num_same(self):
        """test case for when all values are the same"""
        self.assertEqual(reverse_rec([3, 2, 3]), [3, 2, 3])
        self.assertEqual(reverse_rec([4.5, 6.5, 4.5]), [4.5, 6.5, 4.5])
        self.assertEqual(reverse_rec([-5, -3, -5]), [-5, -3, -5])



    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

    def test_bin_search_None(self):
        """test case for when int_list in None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(None, None, None, tlist)

    def test_bin_search_not_found(self):
        """test case for when target is not found"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(11, 0, len(list_val)-1, list_val), None)
        
        

if __name__ == "__main__":
        unittest.main()

    
