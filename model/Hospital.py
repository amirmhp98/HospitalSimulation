from model.Room import Room
from model.Worker import Worker


class Hospital:

    def __init__(self, roomCount, drCountOfRoom):
        self.receptionist = Worker()
        self.rooms = list()
        for i in range(roomCount):
            self.rooms.append(Room(drCountOfRoom[i]))
