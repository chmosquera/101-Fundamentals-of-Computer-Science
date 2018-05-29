#Name: Chanelle Mosquera
#Section: 101-16

import unittest
import logic

class TestCases(unittest.TestCase):
   def test_is_even(self):
      self.assertTrue(logic.is_even(10))
      self.assertFalse(logic.is_even(9))
      pass

   def test_in_an_interval(self):
      self.assertTrue(logic.in_an_interval(2))
      self.assertTrue(logic.in_an_interval(4))
      self.assertFalse(logic.in_an_interval(9))
      self.assertFalse(logic.in_an_interval(47))
      self.assertTrue(logic.in_an_interval(60))
      self.assertFalse(logic.in_an_interval(92))
      self.assertFalse(logic.in_an_interval(12))
      self.assertTrue(logic.in_an_interval(15))
      self.assertTrue(logic.in_an_interval(19))
      self.assertTrue(logic.in_an_interval(101))
      self.assertTrue(logic.in_an_interval(102))
      self.assertTrue(logic.in_an_interval(103))


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

