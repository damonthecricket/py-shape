
try:
	from ..shapes import point
	from ..shapes import shape
except:
	import shapes.point as point
	import shapes.shape as shape

import unittest



# ShapeTest

class ShapeTest(unittest.TestCase):

	def testInstance(self):
		for m in self._instance_mock():
			x = m[0]
			y = m[1]
			s = shape.create(x, y)

			self.assertEqual(s.x(), x)
			self.assertEqual(s.y(), y)


	def testEqual(self):
		for m in self._instance_mock():
			x = m[0]
			y = m[1]
			c = shape.create(x, y)
			s = shape.Shape(x, y)

			self.assertEqual(c, s)


	def _instance_mock(self):
		return [
		([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]), ([4.0, 5.0, 6.0], 	 [4.0, 5.0, 6.0]),
		([7.0, 8.0, 9.0], [7.0, 8.0, 9.0]), ([10.0, 11.0, 12.0], [10.0, 11.0, 12.0])
		]



# PointTest

class PointTest(unittest.TestCase):

	def testInstance(self):
		for m in self._instance_mock():
			x = m[0]
			y = m[1]
			p = point.create(x, y)

			self.assertEqual(p.x(), x)
			self.assertEqual(p.y(), y)


	def testEqual(self):
		for m in self._instance_mock():
			x = m[0]
			y = m[1]
			c = point.create(x, y)
			p = point.Point(x, y)

			self.assertEqual(c, p)


	def _instance_mock(self):
		return [
		(0.0, 0.0), (1.0, 1.0), (2.0, 2.0), (3.0, 3.0), (4.0, 4.0)
		(5.0, 5.0), (6.0, 6.0), (7.0, 7.0), (8.0, 8.0), (9.0, 9.0)
		]



# LineTest

class LineTest(unittest.TestCase):

	def testInstance(self):
		pass
		


# PointTest

class PointTest(unittest.TestCase):

	def testInstance(self):
		pass



