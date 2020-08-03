from functools import total_ordering


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
        self.random_bag = self.distribution.generate_random_numbers(count=100)
        pass


@total_ordering
class Receptionist(Worker):
    def __init__(self, distribution):
        super(Receptionist, self).__init__(distribution)

    def __lt__(self, other):
        if not isinstance(other, Worker):
            raise Exception("bro you are comparing the wrong thing, chill")
        if isinstance(other, Doctor):
            return False
        return True


@total_ordering
class Doctor(Worker):
    def __init__(self, distribution):
        super(Doctor, self).__init__(distribution)
        self.status = "free"  # or 'busy'

    def __lt__(self, other):
        if not isinstance(other, Worker):
            raise Exception("bro you are comparing the wrong thing, chill")
        if isinstance(other, Receptionist):
            return True
        return False



