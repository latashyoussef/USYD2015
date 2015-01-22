# Aspect Ratio

D = 1.0		# Diameter of the sphere
L = 3.2		# Length of the cylinder

def make_row_x(box_length, L, D):
	rod_count = 0
	x = 0
	while x < box_length:
		x = D
		y = L/2.0
		z = D/2.0
		print "%f %f %f \n" % (x, y, z)
		rod_count += 1
		x += D
	return rod_count


