# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This module interfaces with the Quantum Random Number Generator
at the The Australian National University, where it gets a listof
n truly random numbers, converts them to coordinates and computes the
gaussian kernel density estimate of those coordinates, returning the
point within the defined radius, where the density of random coordinates
is highest, similar to how an Attractor point is calculated by Randonautica."""

import argparse
import logging
import math

import numpy as np
import pandas as pd
import quantumrandom
from scipy import stats

__author__ = 'openrandonaut'
__version__ = "0.1.5"

class Error(Exception):
    """Base class for other exceptions"""


class DivisionError(Error):
    """Raised when number of requested point isn't divisible by 1024"""


EARTH_RADIUS = 6371  # km
ONE_DEGREE = EARTH_RADIUS * 2 * math.pi / 360 * 1000  # 1° latitude in meters


def int_to_float(input_integer: int) -> float:
    """Converts an integer to a floating point value"""

    source_bits = int(math.ceil(math.log(1 + 1, 2)))
    source_size = int(math.ceil(source_bits / float(quantumrandom.INT_BITS)))
    source_max = 2 ** (source_size * quantumrandom.INT_BITS) - 1

    modulos = source_max / 1

    while True:
        num = 0
        for _ in range(source_size):
            num <<= quantumrandom.INT_BITS
            num += input_integer

        if num >= modulos:
            return None
        return num / modulos


def pairwise(iterable) -> zip:
    """Returns an iterable in pairs"""

    val = iter(iterable)
    return zip(val, val)


def random_location(
    start_lat: float,
    start_lon: float,
    max_radius: int,
    rand_float_1: float,
    rand_float_2: float,
) -> tuple:
    """Converts 2 floating point values to coordinates within
    the defined radius from the starting position"""

    r_len = max_radius * rand_float_1**0.5
    theta = rand_float_2 * 2 * math.pi
    d_x = r_len * math.cos(theta)
    d_y = r_len * math.sin(theta)

    random_lat = start_lat + d_y / ONE_DEGREE
    random_lon = start_lon + d_x / (ONE_DEGREE * math.cos(start_lat * math.pi / 180))

    return random_lat, random_lon


def calculate_kde(coord_list: list) -> tuple:
    """Calculates the point with the highest density of points
    using kernel density estimation"""

    # Create DataFrame from list of coordinates
    dataframe = pd.DataFrame(coord_list, columns=["longitude", "latitude"])

    y_data = dataframe.latitude
    x_data = dataframe.longitude

    logging.info("Calculating gaussian kernel density estimate...")
    kernel = stats.gaussian_kde(np.vstack([x_data, y_data]), bw_method="silverman")

    # Define grid.
    xmin, xmax = min(x_data), max(x_data)
    ymin, ymax = min(y_data), max(y_data)
    x_val, y_val = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([x_val.ravel(), y_val.ravel()])

    k_pos = kernel(positions)

    max_dense_lat, max_dense_lon = positions.T[np.argmax(k_pos)]
    return (max_dense_lat, max_dense_lon)


def get_coordinate(
    start_lat: float, start_lon: float, radius: int, num_points: int
) -> dict:
    """Takes a starting position, radius and the number of random points to
    base the calculation on, and returns the gaussian kernel desity estimate
    of the generated points as a set of coordinates"""

    if num_points % 1024 != 0:
        raise DivisionError("num_points must be divisible by 1024")

    numbers = []
    for _, value in enumerate(range(int(num_points / 1024))):
        value += 1
        logging.info(
            "Getting %d out of %d random unsigned 16-bit integers from QRNG...",
            1024 * value,
            num_points,
        )
        numbers.extend(
            quantumrandom.get_data(data_type="uint16", array_length=1024, block_size=1)
        )

    logging.info("Converting integers to coordinates... ")
    coord_list = []
    # Iterate over numbers from QRNG in pairs and convert them to coordinates
    for value_1, value_2 in pairwise(numbers):
        value_1 = int_to_float(value_1)
        value_2 = int_to_float(value_2)
        latitude, longitude = random_location(
            start_lat, start_lon, radius, value_1, value_2
        )

        coord_list.append((latitude, longitude))

    max_dense_lat, max_dense_lon = calculate_kde(coord_list)

    logging.info("KDE cordinates: %s, %s", max_dense_lat, max_dense_lon)
    location = (max_dense_lat, max_dense_lon)
    return location


def main():
    """If run as a script, take arguments using argparse and print result to stdout"""

    parser = argparse.ArgumentParser(
        description="This script interfaces with the Quantum Random Number Generator\
                     at the The Australian National University, where it gets a list of\
                     quantum random numbers, converts them to coordinates and computes the\
                     gaussian kernel density estimate of those coordinates, returning the\
                     point within the defined radius, where the density of random coordinates\
                     is highest, similar to how an Attractor point is calculated by Randonautica."
    )

    parser.add_argument(
        "latitude", metavar="LATITUDE", type=float, help="starting position latitude"
    )

    parser.add_argument(
        "longitude", metavar="LONGITUDE", type=float, help="starting position logitude"
    )

    parser.add_argument(
        "-r",
        metavar="RADIUS",
        type=int,
        dest="radius",
        default=5000,
        help="max radius from starting position in meters",
    )

    parser.add_argument(
        "-p",
        metavar="POINTS",
        type=int,
        dest="points",
        default=4096,
        help="number of points to base KDE on (must be divisible by 2014)",
    )

    parser.add_argument(
        "-v", action="store_true", dest="verbose", help="verbose logging"
    )

    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)
        formatter = logging.Formatter("%(message)s")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logging.getLogger().addHandler(console_handler)

    if args.points % 1024 != 0:
        parser.error("Argument POINTS must be divisible by 1024")

    coordinate = get_coordinate(args.latitude, args.longitude, args.radius, args.points)

    if not args.verbose:
        print(f"{coordinate[0]}, {coordinate[1]}")


if __name__ == "__main__":
    main()

