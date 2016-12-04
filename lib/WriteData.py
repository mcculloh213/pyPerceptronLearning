import json
import os

__author__ = "H.D. 'Chip' McCullough IV"


def writeJSON(data, f_in):
    base = os.path.split(f_in)[-1].split('.')[0]                     # Get base file name
    f_out = os.path.join('.', 'weights', base + "_weights.txt")      # Create out file name
    with open(f_out, 'w') as f:
        json.dump(data, f)                                           # Dump JSON to out file


def write_data(data, classification, f_in):
    base = os.path.split(f_in)[-1].split('.')[0]                     # Get base file name
    f_out = os.path.join('.', 'out', base + "_classification.txt")   # Create out file name
    correct = 0
    f = open(f_out, 'w')
    for i in range(len(data)):
        r = data[i]                                                  # Get row of data
        if classification[i] == r[-1]:
            f.write("{0} {1}\n".format(r[1:-1], classification[i]))
            correct += 1
        else:
            f.write("{0} {1} -- Incorrect output\n".format(r[1:-1], classification[i]))
    f.write("Data classified with {0}% accuracy.".format(float(correct / len(data)) * 100))
    f.close()
