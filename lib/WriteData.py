import json
import os

__author__ = "H.D. 'Chip' McCullough IV"


def writeJSON(data, f_in):
    base = os.path.split(f_in)[-1].split('.')[0]                     # Get base file name
    f_out = os.path.join('.', 'weights', base + "_weights.txt")      # Create out file name
    