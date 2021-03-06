import unittest
import poly

class TestPoly(unittest.TestCase):

	def assertListAlmostEqual(self, l1, l2):
		self.assertEqual(len(l1), len(l2))
		for el1, el2 in zip(l1, l2):
			self.assertAlmostEqual(el1, el2)

	def test_poly_add_2_1(self):
		poly1 = [2.3, 4.7, 1.0]
		poly2 = [1.2, 2.1, -3.2]

		poly3 = poly.poly_add2(poly1, poly2)
		self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])

	def test_poly_add2_2(self):
		poly1 = [1, 2, 3]
		poly2 = [4, 5, 6]

		poly3 = poly.poly_add2(poly1, poly2)
		self.assertListAlmostEqual(poly3, [5, 7, 9])

	def test_poly_mult2_1(self):
		poly1 = [1, 2, 3]
		poly2 = [4, 5, 6]

		poly3 = poly.poly_mult2(poly1, poly2)
		self.assertListAlmostEqual(poly3, [4, 13, 28, 27, 18])

	def test_poly_mult2_2(self):
		poly1 = [3, 4, 6]
		poly2 = [1, 7, 3]

		poly3 = poly.poly_mult2(poly1, poly2)
		self.assertListAlmostEqual(poly3, [3, 25, 43, 54, 18])


   # Add tests here

if __name__ == '__main__':
   unittest.main()
