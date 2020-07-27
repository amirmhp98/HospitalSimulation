from model.dto.SimulationContext import SimulationContext


class InitializationServiceImpl:

    def initializeSimulation(self, simulationParameters):
        # todo pass needed params, signatures need to be changed
        hospital = self.initializeHospital()
        matrix = self.initializeMatrix()
        context = SimulationContext(hospital, matrix)
        return context

    def initializeHospital(self):
        # todo implement
        return

    def initializeMatrix(self):
        # todo implement
        return
