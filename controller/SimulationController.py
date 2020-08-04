from service.simulationService import SimulationFlowServiceImpl, InitializationServiceImpl


class SimulationController:

    def __init__(self, number_of_patients=10 ** 7):
        self.number_of_patients = number_of_patients

    def start_process(self):
        """
        method flow:
        1- get inputs
        2- run initializer
        3- run simulation by passing the initializer results
        4- introducing the results to analyzer
        5- showing the results
        """
        print("input simulation data:")
        simulation_parameters = self.get_inputs()
        print("initializing simulation...")
        initializer = InitializationServiceImpl(simulation_parameters, self.number_of_patients)
        simulation_context = initializer.initialize_simulation()
        print("starting simulation...")
        simulator = SimulationFlowServiceImpl()
        simulator.run_simulation(simulation_context)
        # TODO: steps 4 to 5

        pass

    @staticmethod
    def get_inputs():
        # M, landa, alpha, mu = map(float, input().split())
        number_of_rooms, patient_arrival_rate, average_patience, reception_service_rate, = map(float, input().split())
        number_of_rooms = int(number_of_rooms)
        doctors_service_rate = []
        for room_mu_s in range(number_of_rooms):
            doctors_service_rate.append(list(map(float, input().split())))
        return number_of_rooms, patient_arrival_rate, average_patience, reception_service_rate, doctors_service_rate
