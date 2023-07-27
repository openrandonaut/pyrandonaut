Usage
=====

-  .. rubric:: As module
      :name: as-module

   1. Import the module: ``import pyrandonaut``
   2. You can now call the module functions, e.g.:

   .. code:: python

      # Define a starting point
      my_latitude = 51.178840902136464
      my_longitude = -1.8261452442305293

      # Call get_coordinate() with starting point values and store the result
      result = pyrandonaut.get_coordinate(my_latitude, my_longitude)  
      # Print result to screen
      print(f"Go here to escape the stasis field: {result}")

   ``get_coordinate()`` will return a tuple with the calculated
   coordinate. By default it uses a radius of 5000 meters and a value of
   1024 random points to base the calculation on. These values can be
   specified in the arguments.

   -  **Functions and arguments:**

      -  **``get_coordinate()``** is the main functionality of the
         library, generating a coordinate equivalent to an Attractor
         point in Randonautica. It takes the following arguments:

         -  ``start_lat`` Latitude of starting position (float)
         -  ``start_lon`` Longitude of starting position (float)
         -  ``radius`` Max radius from starting position (integer)
         -  ``num_points`` Number of random points to use in calculation
            of kernel density estimate. Must be divisible by 1024
            (integer)

         It returns a tuple in the following format:
         ``(latitude, longitude)``\ 

      -  **``random_location()``** Converts 2 floating point values to
         coordinates within the defined radius from the starting
         position. It takes the following arguments:

         -  ``start_lat`` Latitude of starting position (float)
         -  ``start_lon`` Longitude of starting position (float)
         -  ``radius`` Max radius from starting position (integer)
         -  ``rand_float_1`` Random value to turn into X in coordinate
         -  ``rand_float_2`` Random value to turn into Y in coordinate

         It returns a tuple in the following format:
         ``(latitude, longitude)``

-  .. rubric:: Command-line interface
      :name: command-line-interface

You can also run PyRandonaut directly in your terminal. Example:

.. code:: console

   $ python pyrandonaut.py 51.178840902136464 -1.8261452442305293
   51.20545110291186, -1.824335160309919

Run the script with ``--help`` to see the options:

.. code:: console

      $ python pyrandonaut.py --help                                                                                                                             
      usage: pyrandonaut.py [-h] [-r RADIUS] [-p POINTS] [-v] LATITUDE LONGITUDE
      
      This script interfaces with the Quantum Random Number Generator at Randonautica, where it gets a list of quantum random numbers, converts them to coordinates and computes the gaussian kernel density estimate of those coordinates, returning the point within the defined radius, where the density of random coordinates is highest, similar to how an Attractor point is calculated by the Randonautica app.
      
      positional arguments:
        LATITUDE    starting position latitude
        LONGITUDE   starting position longitude
      
      options:
        -h, --help  show this help message and exit
        -r RADIUS   max radius from starting position in meters
        -p POINTS   number of points to base KDE on (must be divisible by 1024)
        -v          verbose logging
