from model.Worker import Worker


class Room:
    def __init__(self, drCount):
        # todo fill the params (worker params)
        doctors = list()
        coronaQueue = list()
        normalQueue = list()
        for i in range(drCount):
            doctors.append(Worker())
