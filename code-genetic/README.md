# TSP-GA
## Introduction
An implementation of the genetic algorithm for the travelling salesman problem.
The code is constructed in OOP to separate the actual entities and manipulate the variables in each entity on its own.
The accuracy is not as imporessive as I wanted/expected and it turned out to be because of using swapping mutation mainly. Further improvements shall be made in the near future.
For now, the logic and implementation of the genetics algorithm for the travelling salesman problem is proper and it is a matter now of tweaks to apply for better results.


## Standard

All points should be made using the `City` class in `City.py`. Cities are ordered by their index in a list of `n` cities. A solution should be a permutation of numbers from `0` to `n - 1`.

To display a solution graphically, simply `import gui` and call its `draw()` method. Be sure to properly handle the window events such as updating.

# Utilities

## City.py

Contains the `City` class.

### Members:

* `x` - x coordinate; should be between 0 and 1
* `y` - y coordinate; should be between 0 and 1

### Methods:

* `distanceTo(City)` - returns the distance from itself to `City`

## gui.py

Contains the `GUI` class. It used `tkinter` in order to display a window and draw the TSP solution. It does not handle window events by itself.

### Members:

### Methods:

* `draw(cities, populationFittest)` - draws all points from `cities` and connects them with a line in the order specified in `populationFitteset`

# Algorithms

### GeneticAlgorithm.py

A TSP genetic algorithm with the following mutation:

* Swapping two points

It has hardcoded parameters that solve an instance of TSP with a random uniform distribution of 100 points in under 1 minute on a modern computer.

Make sure `gui.py` and `City.py` are included in the directory.

## Usage

`python gui.py <Name of a file in .TSP format>`
### Inspiration
The algorithm was written as a sort of practice and understanding of genetic algorithm and how it should work to optimize 
any NP-problem later on. The implementation is based on an article "Applying a genetic algorithm to the traveling salesman problem" by  LEE JACOBSON.

## Bugs
Currently working on fixing some bugs and setting the algorithm for a higher optimization fitness score.


