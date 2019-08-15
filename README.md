# PyShape
[![codebeat badge](https://codebeat.co/badges/7b027dab-df0c-4a50-8853-64b3a4be1786)](https://codebeat.co/projects/github-com-damonthecricket-pyshape-master) [![Build Status](https://travis-ci.org/damonthecricket/pyshape.svg?branch=master)](https://travis-ci.org/damonthecricket/pyshape)



Python language shape plot library.


1. [Features](#features)
2. [Installation](#installation)



### Features
1. Feagure. Tiny module to create empty plot figure.
   ```python
   import pyshape.figure as figure
   
   # Creates and shows empty plot figure with Test figure title.
	 fgr = figure.create("Test figure.")
   fgr.show()
   ```
2. Axe. Tiny module to manage figure axises.
   ```python
   import pyshape.figure as figure
   import pyshape.axe as axe
   
   fgr = figure.create("Test figure.")
   
   # Creates and sets x, y axises to figure.
	 fgr.set_x_axe( axe.create([1, 2], ["June", "Jule"]) )
	 fgr.set_y_axe( axe.create([1, 2, 3], [1, 2, 3]) )
   ```
 3. Plot. Tiny module to create figure subplot.
   ```python
   import pyshape.figure as figure
   import pyshape.plot as plot
   
	 fgr = figure.create("Test figure.")
  
   # Creates figure subplot with 1, 1, 1 proportions.
	 sp = fgr.subplot(1, 1, 1)
   
   # Sets x, y axises labels.
	 sp.set_x_label("x")
	 sp.set_y_label("y")
   ```
 4. Line. Tiny module to draw line.
   ```python
   import pyshape.figure as figure
   import pyshape.plot as plot
   import pyshape.shape.line as line
   
	 fgr = figure.create("Test figure.")
  
	 sp = fgr.subplot(1, 1, 1)
   
   # Creates and shows line from 0.0, 0.0 to 3.0, 3.0 coordinates.
   sp.set_shape( line.create(point.create(0.0, 0.0), point.create(3.0, 3.0)) )
   fgr.show()
   ``` 
 5. Rect. Tiny module to draw rectagle
   ```python
   import pyshape.figure as figure
   import pyshape.plot as plot
   import pyshape.shape.rect as rect
   
	 fgr = figure.create("Test figure.")
  
	 sp = fgr.subplot(1, 1, 1)
   
   # Creates and shows rect with start point at 1.0, 1.0 and 1.0 width and height.
   sp.set_shape( rect.create(point.create(1.0, 1.0), 1.0, 1.0) )
   fgr.show()
   ``` 
   
   
   
  ### Installation
  ```
  $ git clone https://github.com/damonthecricket/pyshape.git
  ```
