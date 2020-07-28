class Worker:
    def __init__(self, distribution):
        self.distribution = distribution
        self.random_bag = []

    def get_next_random_duration(self):
        """
        if reached end of random bag index, fillRandomBag()
        return randomBag.get(currentIndex++)
        """
        if not self.random_bag:
            self.fill_random_bag()
        return self.random_bag.pop()

    def fill_random_bag(self):
        """
        get next 100 random numbers and store them in random bag
        currentIndex = 0
        """
        # TODO: implement
        # self.random_bag = self.distribution.generate_random_numbers(count=100)
        pass


class Receptionist(Worker):
    def __init__(self, distribution):
        super(Receptionist, self).__init__(distribution)


class Doctor(Worker):
    def __init__(self, distribution):
        super(Doctor, self).__init__(distribution)
