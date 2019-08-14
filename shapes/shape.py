


# Create

def create(x = [], y = []):
	return Shape(x, y)



class Shape:

	def __init__(self, x = [], y = []):
		self._x = x
		self._y = y


	def x(self):
		return self._x


	def y(self):
		return self._y


	def __eq__(self, other):
		return self._x == other.x() and self._y == other.y()


	def __str__(self):
		return "Shape class, x = %s, y = %s" % (self.x(), self.y())
		