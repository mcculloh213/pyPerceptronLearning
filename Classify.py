import json
import numpy
import os
import sys
import lib.ReadData
import lib.NeuralNetwork
import lib.WriteData

from lib.HevisideStepFunction import theta

__author__ = "H.D. 'Chip' McCullough IV"

# DataSetI:   (!x1 && !x2) || (x1 && !x2)
# DataSetII:  (x1 && x2) || (x1 && x3) || (x2 && x3)
# DataSetIII: !x1 && (x2 ^ x3) || x1 && (!x2 && !x3 || x2 && x3)
# DataSetIV:  x1 ^ x2 -- XOR

if __name__ == '__main__':
    f_in = sys.argv[1]                                                    # Get input from shell
    if os.path.exists(f_in):
        pth = os.path.split(f_in)
        d = os.path.join('.', 'data', pth[1].split('_')[0] + '.txt')
        N, data = lib.ReadData.read_data(d)                               # Read input data
        f = open(f_in)
        weights = json.load(f)                                            # Read weight file
        w = [weights['wb']]                                               # Initialize weights with wb
        for i in range(1, N):
            w.append(weights['w{0}'.format(i)])
        E = []                                                            # Classification vector
        for row in data:
            E.append(theta(float(numpy.dot(row[:len(row) - 1], w))))      # Vector dot product data and weights

        lib.WriteData.write_data(data, E, f_in)
    else:
        print("File {0} not found.")

