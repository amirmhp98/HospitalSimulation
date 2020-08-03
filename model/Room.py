from queue import Queue


class Room:
    def __init__(self, doctors):
        # todo fill the params (worker params)
        self.doctors = doctors
        self.corona_queue = Queue()
        self.normal_queue = Queue()
