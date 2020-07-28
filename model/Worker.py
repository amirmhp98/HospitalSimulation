class Worker:
    def __init__(self, distribution):
        self.distribution = distribution

    def getNextRandomDuration(self):
        """
        if reached end of random bag index, fillRandomBag()
        return randomBag.get(currentIndex++)
        """
        pass

    def fillRandomBag(self):
        """
        get next 100 random numbers and store them in random bag
        currentIndex = 0
        """
        pass


class Receptionist(Worker):
    def __init__(self, distribution):
        super(Receptionist, self).__init__(distribution)


class Doctor(Worker):
    def __init__(self, distribution):
        super(Doctor, self).__init__(distribution)
