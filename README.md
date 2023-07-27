## PyRandonaut
![Python](https://img.shields.io/badge/built%20with-Python3-red.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

### Open-source quantum random coordinate generation for randonauts ❤️
<img align="left" src="https://i.imgur.com/RJxATsu.png" width="170">

**pyrandonaut** is a Python3 module for generating quantum random coordinates. It interfaces with a QRNG (Quantum Random Number Generator) where it gets a list of [quantum random](https://en.wikipedia.org/wiki/Hardware_random_number_generator#Quantum_random_properties) numbers, converts them to coordinates and then computes the [gaussian kernel density estimate](https://en.wikipedia.org/wiki/Kernel_density_estimation) of those coordinates to find a point with a statistically anomalous density, similar to how an Attractor point is generated by [Randonautica](https://www.randonautica.com/).
	<br><br>
	This gives you the ability to implement quantum random coordinates in your own applications. Just `import pyrandonaut` and off you go!
	<br><br>
	If you're unfamiliar with Randonautica, the concepts of Probability Blind-Spots and Quantum Randomness, I recommend reading [fatum_theory.txt](https://github.com/anonyhoney/fatum-en/blob/master/docs/fatum_theory.txt) which shipped with the original Fatum Project bot that inspired Randonautica. [This video](https://www.youtube.com/watch?v=6C6aXta3m1M) gives a lot of great background info too. If you have no idea what any of this is about and is completely new to this, watch [this video](https://www.youtube.com/watch?v=nDX81AUm8yE) and/or read [this article](https://medium.com/swlh/randonauts-how-a-random-number-generator-can-set-you-free-dfc2a2413e15).

Contributions greatly appreciated!

## Table of contents
* [Introduction](#openrandonaut)
* [Installation](#installation)
* [Usage](#usage)
	* [As module](#as-module)
	* [Command line interface](#command-line-interface)
* [Visualization](#visualization)
* [To-do](#to-do)

## Installation
The module requires at least Python 3.9 to function and can be installed using [pip](https://pip.pypa.io/en/stable/) like so:<br>
`pip install pyrandonaut`
<br><br>
That's it!


## Usage

* ### As module

	1. Import the module: `import pyrandonaut`
	2. You can now call the module functions, e.g.:<br>
	
	```python
	# Define a starting point
	my_latitude = 51.178840902136464
	my_longitude = -1.8261452442305293
	
	# Call get_coordinate() with starting point values and store the result
	result = pyrandonaut.get_coordinate(my_latitude, my_longitude)	
	# Print result to screen
	print(f"Go here to escape the stasis field: {result}")
	``` 
	`get_coordinate()` will return a tuple with the calculated coordinate. By default it uses a radius of 5000 meters and a value of 1024 random points to base the calculation on. These values can be specified in the arguments.
	
	* **Functions and arguments:**
		* **`get_coordinate()`** is the main functionality of the library, generating a coordinate equivalent to an Attractor point in Randonautica. It takes the following arguments:
			* `start_lat` Latitude of starting position (float)
			* `start_lon` Longitude of starting position (float)
			* `radius` Max radius from starting position (integer)
			* `num_points` Number of random points to use in calculation of kernel density estimate. Must be divisible by 1024 (integer)
		
			It returns a tuple in the following format:<br>
			`(latitude, longitude)`<br>
		
		* **`random_location()`** Converts 2 floating point values to coordinates within
    the defined radius from the starting position. It takes the following arguments:
			* `start_lat` Latitude of starting position (float)
			* `start_lon` Longitude of starting position (float)
			* `radius` Max radius from starting position (integer)
			* `rand_float_1`	Random value to turn into X in coordinate
			* `rand_float_2`	Random value to turn into Y in coordinate
			
			It returns a tuple in the following format:<br>
			`(latitude, longitude)`
		
* ### Command-line interface

 You can also run PyRandonaut directly in your terminal.
 Example:
 
 ```console
 $ python pyrandonaut.py 51.178840902136464 -1.8261452442305293
 51.20545110291186, -1.824335160309919
 ```
 
 Run the script with `--help` to see the options:
 
 ```console
	$ python pyrandonaut.py --help                                                                                                                             
	usage: pyrandonaut.py [-h] [-r RADIUS] [-p POINTS] [-v] LATITUDE LONGITUDE
	
	This application interfaces with a QRNG (Quantum Random Number Generator) where it gets a list of
	quantum random numbers, converts them to coordinates and computes the gaussian kernel density estimate of those coordinates, returning the point within the defined radius, where the density of random coordinates is highest, similar to how an Attractor point is calculated by Randonautica.
	
	positional arguments:
	  LATITUDE    starting position latitude
	  LONGITUDE   starting position longitude
	
	options:
	  -h, --help  show this help message and exit
	  -r RADIUS   max radius from starting position in meters
	  -p POINTS   number of points to base KDE on (must be divisible by 1024)
	  -v          verbose logging

```


## Visualization
<img src="https://camo.githubusercontent.com/e6b5661fff27ec6a7e51f39141e640bf8c59c9d05b7847e28af71d32ddcb06fc/68747470733a2f2f692e696d6775722e636f6d2f427878786464462e706e67" alt="Heatmap" style="width:50%"><br>This is a heatmap visualization of how the module calculates the Attractor point. An arbitrary number of points based on QRNG numbers are plotted geospatially and the place with the highest density of points is returned.  Image made using [Seaborn](https://github.com/mwaskom/seaborn) and [this script](https://github.com/openrandonaut/openrandonaut/blob/main/kdeplot_heatmap.py) (BETA).


## To-do
- [ ] Migrate _all_ documentation to docstrings/type hints for Sphinx auto generation
- [ ] Add more QRNG sources (If you can help supply hardware modules for testing, please get in touch!)
- [ ] Implement asynchronous requests
- [ ] Implement heatmap generation from [openrandonaut-bot](https://github.com/openrandonaut/openrandonaut-bot)
- [ ] Add ability to calculate Void and Power points as well
