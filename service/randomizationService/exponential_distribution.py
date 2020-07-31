import numpy as np


class ExponentialDistribution:
    def __init__(self, parameter):
        self.parameter = parameter

    def generate_random_numbers(self, count):
        return np.random.exponential(scale=self.parameter, size=count)
