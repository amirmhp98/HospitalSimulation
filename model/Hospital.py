from model.Room import Room
from model.Worker import Worker


class Hospital:

    def __init__(self, receptionist, rooms):
        self.receptionist = receptionist
        self.rooms = rooms
