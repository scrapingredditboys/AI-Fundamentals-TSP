# Standard

All points should be made using the `Point` class in `point.py`. Points are ordered by their index in a list of `n` points. A solution should be a permutation of numbers from `0` to `n - 1`.

To display a solution graphically, simply `import gui` and call its `draw()` method. Be sure to properly handle the window events such as updating.

# Utilities

## point.py

Contains the `Point` class.

### Members:

* `x` - x coordinate; should be between 0 and 1
* `y` - y coordinate; should be between 0 and 1

### Methods:

* `getDistance(point)` - returns the distance from itself to `point`

## gui.py

Contains the `GUI` class. It used `tkinter` in order to display a window and draw the TSP solution. It does not handle window events by itself.

### Members:

### Methods:

* `draw(points, solution)` - draws all points from `points` and connects them with a line in the order specified in `solution`

# Algorithms

## sa.py

A sample simulated annealing algorithm containing three mutations:

* Swapping two points
* Inserting a point elsewhere
* Reversing a subpath of a solution

It has hardcoded parameters that solve an instance of TSP with a random uniform distribution of 100 points in under 30 seconds on a modern computer.

Make sure `gui.py` and `point.py` are included in the directory.

### Usage

`python sa.py`