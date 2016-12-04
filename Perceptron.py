import numpy
import os
import sys
import subprocess
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
    subprocess.run(['python3', 'Learn.py', f_in])                    # Execute Learn.py
    w_file = os.path.join('.', 'weights', os.path.split(f_in)[1].split('.')[0] + '_weights.txt')
    subprocess.run(['python3', 'Classify.py', w_file])               # Execute Classify.py
