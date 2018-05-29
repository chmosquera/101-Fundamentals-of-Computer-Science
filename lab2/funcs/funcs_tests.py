import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
      self.assertEqual(funcs.f(2), 32)
      pass


   def test_f_2(self):
      self.assertEqual(funcs.f(5), 185)
      pass
  
   def test_g_1(self):
      self.assertEqual(funcs.g(6,6), 4)
      pass

   def test_g_2(self):
      self.assertEqual(funcs.g(3,9), 10)
      pass

   def test_hypotenuse(self):
      self.assertEqual(funcs.hypotenuse(4,3), 5)
      self.assertEqual(funcs.hypotenuse(7,5), 8.6023252670426267)
      pass

   def test_is_positive(self):
      self.assertTrue(funcs.is_positive(3),True)
      self.assertFalse(funcs.is_positive(-1), False)
      pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

