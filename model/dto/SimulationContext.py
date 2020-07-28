class SimulationContext:

    def __init__(self, hospital, simulationMatrix, patience):
        self.hospital = hospital
        self.simulationMatrix = simulationMatrix
        self.patience = patience
        self.reception_queue_history = {}  # keeps length of queue at given times
        self.rooms_queue_history = [{} for _ in range(len(hospital.rooms))]

