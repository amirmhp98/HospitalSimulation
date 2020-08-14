from numpy import var
from math import ceil, sqrt

from service.analyzeService.VisualAnalyzerService import VisualAnalyzerService
from service.simulationService.SimulationFlowServiceImpl import SimulationFlowServiceImpl
from service.simulationService.InitializationServiceImpl import InitializationServiceImpl


class AnalyzeServiceImpl:

    def __init__(self, simulation_context, number_of_patients, simulation_parameters):
        self.reception_queue_history = simulation_context.reception_queue_history
        self.rooms_queue_history = simulation_context.rooms_queue_history
        self.simulation_matrix = simulation_context.simulation_matrix
        self.number_of_patients = number_of_patients
        self.simulation_parameters = simulation_parameters

    def run(self):
        # average_time_spent_in_system = self.calculate_average_time()
        # print(f"average_time_spent_in_system = {average_time_spent_in_system}")
        # average_corona_time_spent_in_system = self.calculate_average_time(patient_type='corona')
        # print(f"average_corona_time_spent_in_system = {average_corona_time_spent_in_system}")
        # average_normal_time_spent_in_system = self.calculate_average_time(patient_type='normal')
        # print(f"average_normal_time_spent_in_system = {average_normal_time_spent_in_system}")
        # average_waiting_time_in_queue = self.calculate_average_time(req='time_waited_in_queue')
        # print(f"average_waiting_time_in_queue = {average_waiting_time_in_queue}")
        # average_corona_waiting_time_in_queue = self.calculate_average_time(patient_type='corona',
        #                                                                    req='time_waited_in_queue')
        # print(f"average_corona_waiting_time_in_queue = {average_corona_waiting_time_in_queue}")
        # average_normal_waiting_time_in_queue = self.calculate_average_time(patient_type='normal',
        #                                                                    req='time_waited_in_queue')
        # print(f"average_normal_waiting_time_in_queue = {average_normal_waiting_time_in_queue}")
        number_of_leaved_patients = self.calculate_number_of_leaved_patients()
        print(f"number_of_leaved_patients = {number_of_leaved_patients}")
        average_reception_queue_length = average(self.reception_queue_history)
        print(f"average_reception_queue_length = {average_reception_queue_length}")
        average_first_room_queue_length = average(self.rooms_queue_history[0])
        print(f"average_first_room_queue_length = {average_first_room_queue_length}")
        average_second_room_queue_length = average(self.rooms_queue_history[1])
        print(f"average_second_room_queue_length = {average_second_room_queue_length}")
        # self.calculate_simulation_precision()
        self.find_best_doctor_service_time()
        print("plotting diagrams...")
        visualAnalyzer = VisualAnalyzerService(self.simulation_matrix)
        visualAnalyzer.plot_diagrams()

    def calculate_average_time(self, patient_type='all', req='time_spent_in_system'):
        if patient_type == 'corona':
            corona_queue = [patient[req] for patient in self.simulation_matrix if patient['type'] == 'corona']

            return sum(corona_queue)/len(corona_queue)
        elif patient_type == 'normal':
            normal_queue = [patient[req] for patient in self.simulation_matrix if patient['type'] == 'normal']
            return sum(normal_queue)/len(normal_queue)
        else:
            return sum([patient[req] for patient in self.simulation_matrix]) / len(self.simulation_matrix)

    def calculate_number_of_leaved_patients(self):
        return sum([1 for patient in self.simulation_matrix if patient['did_leave']])

    def calculate_simulation_precision(self):
        waiting_time_history = [patient['time_waited_in_queue'] for patient in self.simulation_matrix]
        variance = var(waiting_time_history)
        average_wait_time = sum(waiting_time_history) / len(waiting_time_history)
        # print(variance, average_wait_time)
        precision = 1.96 * sqrt(variance) / (average_wait_time * sqrt(self.number_of_patients))
        print(f"precision: {precision * 100}")

    def find_best_doctor_service_time(self):
        max_queue_length = 3
        final_service_rates = []
        new_simulation_parameters = self.simulation_parameters
        while max_queue_length > 1:
            new_doctor_service_rate = [
                [doctor_service_rate - 1 if doctor_service_rate > 1 else 1 for doctor_service_rate in
                 room_service_rates]
                for room_service_rates in new_simulation_parameters[4]]
            new_simulation_parameters = self.simulation_parameters[0], self.simulation_parameters[1], \
                                        self.simulation_parameters[2], self.simulation_parameters[3], \
                                        new_doctor_service_rate
            initializer = InitializationServiceImpl(new_simulation_parameters, number_of_patients=100000)
            simulation_context = initializer.initialize_simulation()
            simulator = SimulationFlowServiceImpl()
            simulated_context = simulator.run_simulation(simulation_context)
            max_room_queue_lengths = [max(room_queue_history.values()) for room_queue_history in simulated_context.rooms_queue_history]
            max_queue_length = max(max_room_queue_lengths)
            final_service_rates = initializer.doctors_service_rate

        print(f"doctor service rates that makes queue empty: {final_service_rates}")


def average(items):
    if len(items) == 0:
        return 0
    return sum(items.values()) / len(items)
