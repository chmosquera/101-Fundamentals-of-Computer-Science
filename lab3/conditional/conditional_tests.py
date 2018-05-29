import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_max101(self):
      self.assertEqual(conditional.max_101(10,9), 10)
      self.assertEqual(conditional.max_101(8,9), 9)
      pass

   def test_max_of_three(self):
      self.assertEqual(conditional.max_of_three(float(10),float(9),float(8)), 10.0)
      self.assertEqual(conditional.max_of_three(float(9),float(10),float(8)), 10.0)
      self.assertEqual(conditional.max_of_three(float(8),float(9),float(10)), 10.0)
      pass

   def test_rental_late_fee(self):
      self.assertEqual(conditional.rental_late_fee(0), 0)
      self.assertEqual(conditional.rental_late_fee(5), 5)
      self.assertEqual(conditional.rental_late_fee(9), 5)
      self.assertEqual(conditional.rental_late_fee(11), 7)
      self.assertEqual(conditional.rental_late_fee(15), 7)
      self.assertEqual(conditional.rental_late_fee(18), 19)
      self.assertEqual(conditional.rental_late_fee(24), 19)
      self.assertEqual(conditional.rental_late_fee(26), 100)
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
