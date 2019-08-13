
from . import point



# Line

def create(start, end):
	return Line(start, end)



class Line:

	def __init__(self, start, end):
		self._start = start
		self._end = end


	def start(self):
		return self._start


	def end(self):
		return self._end

		
		

