from service.InputService.InputServiceImpl import InputServiceImpl
from service.analyzeService.AnalyzeServiceImpl import AnalyzeServiceImpl
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
        simulation_parameters = InputServiceImpl().get_inputs()
        print("initializing simulation...")
        initializer = InitializationServiceImpl(simulation_parameters, self.number_of_patients)
        simulation_context = initializer.initialize_simulation()
        print("starting simulation...")
        simulator = SimulationFlowServiceImpl()
        simulated_context = simulator.run_simulation(simulation_context)
        print("starting analyze simulation...")
        analyser = AnalyzeServiceImpl(simulated_context, self.number_of_patients, simulation_parameters)
        analyser.run()
        pass

