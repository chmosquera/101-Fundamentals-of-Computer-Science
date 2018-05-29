# Name: Chanelle Mosquera
# Section: 101-16
# Description of program: List Indexing
# Instructor: S. Einakian
# Due date: 02/02/16

poly1 = [1,2,3]
poly2 = [4,5,6]

#function takes two polynomials of degree two (lists of length 3) as arguments
def poly_add2(poly1,poly2): 
	poly3 = [poly1[0] + poly2[0], poly1[1] + poly2[1], poly1[2] + poly2[2]]
	return poly3

def poly_mult2(poly1, poly2):
	A1 = poly1[0]
	B1 = poly1[1]
	C1 = poly1[2]
	A2 = poly2[0]
	B2 = poly2[1]
	C2 = poly2[2]
	poly3 = [A1*A2, A1*B2 + B1*A2, A1*C2 + B1*B2 + C1*A2, B1*C2 + C1*B2, C1*C2] 
	return poly3



print poly_mult2(poly1, poly2)
