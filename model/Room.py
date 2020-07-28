from model.Worker import Worker


class Room:
    def __init__(self, doctors):
        # todo fill the params (worker params)
        self.doctors = doctors
        self.corona_queue = list()
        self.normal_queue = list()
