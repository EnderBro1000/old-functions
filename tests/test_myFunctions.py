import numpy as np
from .. import myFunctions

def test_printMatrix():
    np.fill((8, 8), 0)
    assert myFunctions.printMatrix()