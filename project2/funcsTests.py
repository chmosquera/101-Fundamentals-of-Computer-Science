import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1_1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc1_2(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 1), -1.296)

   def test_update_alt_2(self):
      self.assertAlmostEqual(updateAltitude(1.0, 2.0, 3.0), 4.5)
   def test_update_alt_2(self):
      self.assertAlmostEqual(updateAltitude(5.0, 1.0, 2.0), 7.0)

   def test_update_vel_1(self):
      self.assertAlmostEqual(updateVelocity(5.0, 4.0), 9.0) 
   def test_update_vel_2(self):
      self.assertAlmostEqual(updateVelocity(2.0, 12.0), 14.0) 

   def test_update_fuel_1(self):
      self.assertAlmostEqual(updateFuel(4,  3), 1) 
   def test_update_fuel_2(self):
      self.assertAlmostEqual(updateFuel(12,  5), 7) 
      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

