
try:
	from ..shapes import point
	from ..shapes import shape
	from ..shapes import line
	from ..shapes import rect
except:
	import shapes.point as point
	import shapes.shape as shape
	import shapes.line as line
	import shapes.rect as rect

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
		for m in self._instance_mock():
			s = m[0]
			e = m[1]
			l = line.create(s, e)

			self.assertEqual(l.start(), s)
			self.assertEqual(l.end(), e)


	def testEqual(self):
		for m in self._instance_mock():
			s = m[0]
			e = m[1]
			c = line.create(s, e)
			l = line.Line(s, e)

			self.assertEqual(c, l)


	def testBuffer(self):
		for m in self._instance_mock():
			s = m[0]
			e = m[1]
			l = line.create(s, e)

			self.assertEqual(l.x(), [s.x(), e.x()])
			self.assertEqual(l.y(), [s.y(), e.y()])


	def _instance_mock(self):
		return [
		(point.create(0.0, 0.0), point.create(1.0, 1.0)),
		(point.create(2.0, 2.0), point.create(3.0, 3.0)),
		(point.create(4.0, 4.0), point.create(5.0, 5.0)),
		(point.create(6.0, 6.0), point.create(7.0, 7.0))
		]
		


# RectTest

class RectTest(unittest.TestCase):

	def testInstance(self):
		for m in self._instance_mock():
			s = m[0]
			w = m[1]
			h = m[2]
			r = rect.create(s, w, h)

			self.assertEqual(r.start(), s)
			self.assertEqual(r.width(), w)
			self.assertEqual(r.height(), h)


	def testEqual(self):
		for m in self._instance_mock():
			s = m[0]
			w = m[1]
			h = m[2]
			c = rect.create(s, w, h)
			r = rect.Rect(s, w, h)

			self.assertEqual(c, r)


	def testBuffer(self):
		for m in self._instance_mock():
			s = m[0]
			w = m[1]
			h = m[2]
			r = rect.create(s, w, h)

			self.assertEqual(r.x(), [s.x(), s.x() + w, s.x() + w, s.x()])
			self.assertEqual(r.y(), [s.y(), s.y(), s.y() + h, s.y() + h])


	def _instance_mock(self):
		return [
		(point.create(0.0), 1.0, 1.0),
		(point.create(1.0), 2.0, 2.0),
		(point.create(2.0), 3.0, 3.0),
		(point.create(3.0), 4.0, 4.0)
		]


# PointTest

class PointTest(unittest.TestCase):

	def testInstance(self):
		pass



