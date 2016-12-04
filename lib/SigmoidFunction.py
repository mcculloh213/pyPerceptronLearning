import math

__author__ = "H.D. 'Chip' McCullough IV"


def g(x):
    """
    Sigmoid Functiong for neuron activation
    :param x: parameter
    :type x: float
    :return: float in [0, 1]
    """
    return 1.0/(1.0 + math.exp(x*-1))
