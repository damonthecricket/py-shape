
try:
	from . import figure
	from . import axe

	from .shapes import line
	from .shapes import point
	from .rect import rect
except Exception as e:
	import figure
	import axe
	import shapes.line as line
	import shapes.point as point
	import shapes.rect as rect



if __name__ == '__main__':
	fgr = figure.create("Test figure.")

	fgr.set_x_axe( axe.create([1, 2], ["June", "Jule"]) )
	fgr.set_y_axe( axe.create([1, 2, 3], [1, 2, 3]) )

	sp = fgr.subplot(1, 1, 1)
	sp.set_x_label("x")
	sp.set_y_label("y")
	
	sp.set_shape( line.create(point.create(0.0, 0.0), point.create(3.0, 3.0)) )
	sp.set_shape( rect.create(point.create(1.0, 1.0), 1.0, 1.0) )

	fgr.show()