import scipy as sp
from scipy.stats import poisson


class PoissonDistribution:
    def __init__(self, parameter):
        self.random_numbers = []
        self.parameter = parameter

    def generate_random_numbers(self, count):
        self.random_numbers = list(poisson.rvs(mu=self.parameter, size=count))
        # self.random_numbers = sp.rand.poisson(lam=self.parameter, size=count)

        return self.random_numbers

    def get_arrival_times(self, init_time):
        arrival_times = [init_time]
        for index, random in enumerate(self.random_numbers):
            arrival_times.append(arrival_times[index] + random)
        return arrival_times[1:]
