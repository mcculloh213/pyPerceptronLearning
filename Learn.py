import numpy
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
    f_in = sys.argv[1]                                               # Get input from shell

    # -------------------------------------------LEARN------------------------------------------- #
    lim = 10000                                                      # Set the epoch limit
    alpha = 0.5                                                      # Set learning rate
    N, data = lib.ReadData.read_data(f_in)                           # Read input data
    w = numpy.random.rand(N)                                         # Initialize random weight vector
    wp = w.copy()                                                    # Copy w into w'
    for i in range(0, lim):
        x = lib.NeuralNetwork.epoch(data, wp, alpha)                 # Iterate through data, adjusting weights
        if numpy.array_equal(x, wp):                                 # If weights did not change in iteration
            break                                                        # Weights have been found
        else:                                                        # If weights changed
            wp = x.copy()                                                # Update w'
    weights = {'wb': wp[0]}                                          # Initialize weights dictionary -- JSON
    for i in range(1, len(wp)):
        weights['w{0}'.format(i)] = wp[i]

    # -------------------------------------------WRITE------------------------------------------- #
    lib.WriteData.writeJSON(weights, f_in)                           # Write JSON to a file in weights dir
