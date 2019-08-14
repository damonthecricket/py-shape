
from . import point
from . import shape



# Rect

def create(start, width, height):
	return Rect(start, width, height)
		

class Rect(shape.Shape):

	def __init__(self, start, width, height):
		shape.Shape.__init__(self, [start.x(), start.x() + width, start.x() + width, start.x(), start.x()],
							[start.y(), start.y(), start.y() + height, start.y() + height, start.y()])

		self._start = start
		self._width = width
		self._height = height


	def start(self):
		return self._start


	def width(self):
		return self._width


	def height(self):
		return self._height


	def __eq__(self, other):
		return self._start == other.start() and self._width == other.width() and self._height == other.height()


	def __str__(self):
		return "Rect shape, start %s, width %s, height %s" % (self.start(), self.width(), self.height())
		

