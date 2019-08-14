
try:
	from . import figure
except Exception as e:
	import figure



if __name__ == '__main__':
	fgr = figure.create("Test figure.")
	fgr.show()