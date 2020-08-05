import numpy as np
from math import ceil


class ExponentialDistribution:
    def __init__(self, parameter):
        self.parameter = parameter

    def generate_random_numbers(self, count):
        return list(map(ceil, np.random.exponential(scale=self.parameter, size=count)))
