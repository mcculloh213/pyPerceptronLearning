import numpy
import lib.HevisideStepFunction as hsf
import lib.SigmoidFunction as sgm

__author__ = "H.D. 'Chip' McCullough IV"


def update(w, alph, err, x):
    """
    Update
    :param w: Weight vector
    :param alph: Learning rate
    :param err: Error
    :param x: Data vector
    :return: w'
    """
    return w + alph * err * numpy.array(x)


def epoch(data, weights, alpha):
    """
    One pass through data to update weights and error.
    :param data: Dataset
    :param weights: Weight vector
    :param alpha:Learning rate
    :return: (w', e')
    """
    for dset in data:
        x = dset[:len(dset)-1]                                       # Get input vector
        E = dset[-1]                                                 # Get expected value
        a = sgm.g(float(numpy.dot(x, weights)))                  # Calculate output
        error = float(E - a)                                         # Calculate error
        weights = update(weights, alpha, error, x)                   # Update weights

    return weights
