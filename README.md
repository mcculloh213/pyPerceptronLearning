# pyPerceptronLearning
_Author: H.D. "Chip" McCullough IV_

## About
Python solution for Programming Assignment 05. There are multiple ways to execute the perceptron. The first way is to first execute the command:
``` shell
    $ python3 Learn.py "./data/<DATA SET>.txt"
```
Next, execute:
``` shell
    $ python3 Classify.py "./weights/<DATA SET>_weights.txt"
```
The first script, `Learn.py` reads the data file, and writes the learned weight file for the data set. `Classify.py` then takes that weight file and attempts to 
classify its respective data set. The output is then logged in the `./out` directory.

The second way to execute the perceptron merges the above commands into one by executing:
``` shell
    $ python3 Perceptron.py "./data/<DATA SET>.txt"
```
The script `Perceptron.py` uses the `subprocess` library to execute the above two commands within the script.

This solution was built using Python 3.5