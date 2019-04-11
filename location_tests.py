import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        """test case for repr method"""
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")
        loc2 = Location("New York", 40.7, 74.0)
        self.assertEqual(repr(loc2),"Location('New York', 40.7, 74.0)")
        loc3 = Location("LA", 34.05, 118.24)
        self.assertEqual(repr(loc3),"Location('LA', 34.05, 118.24)")
    
    # Add more tests!
    def test_eq(self):
        """test case for eq method"""
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1, Location("SLO", 35.3, -120.7))
        loc2 = Location("New York", 40.71, 74.00)
        self.assertEqual(loc2, Location("New York", 40.71, 74.00))
        loc3 = Location("LA", 34.05, 118.24)
        self.assertEqual(loc3, Location("LA", 34.05, 118.24))

    def test_eq_wrong_type(self):
        """test case for when Location is compared with other type"""
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertFalse(loc1 == "San Luis Obispo")   # expects False

    def test_eq_wrong_name(self):
        """test case for when lat and lon are the same and name is different"""
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc1, Location("San Luis Obispo", 35.3, -120.7))   # expects False

    def test_eq_different_lat(self):
        """test case for when lon and name are the same and lat is different"""
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc1, Location("SLO", 36, -120.7))   # expects False

    def test_eq_different_lon(self):
        """test case for when lat and name are the same and lon is different"""
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc1, Location("SLO", 35.3, -121))   # expects False
        

if __name__ == "__main__":
        unittest.main()
