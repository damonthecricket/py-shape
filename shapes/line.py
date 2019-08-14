
from . import point
from . import shape



# Line

def create(start, end):
	return Line(start, end)



class Line(shape.Shape):

	def __init__(self, start, end):
		shape.Shape.__init__(self, [start.x(), end.x()], [start.y(), end.y()])

		self._start = start
		self._end = end
		

	def start(self):
		return self._start


	def end(self):
		return self._end


	def __eq__(self, other):
		return self._start == other.start() and self._end == other.end()


	def __str__(self):
		return "Line class, start %s, end %s" % (self._start, self._end)

		
		

