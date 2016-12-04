__author__ = "H.D. 'Chip' McCullough IV"


def theta(x):
    """
    Heviside Step Function
    :param x: parameter
    :type x: float
    :return: 0 or 1
    """
    return 0 if x < 0 else 1
