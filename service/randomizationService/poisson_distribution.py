import scipy as sp


class PoissonDistribution:
    def __init__(self, parameter):
        self.parameter = parameter

    def generate_random_numbers(self, count):
        return sp.rand.poisson(lam=self.parameter, size=count)
