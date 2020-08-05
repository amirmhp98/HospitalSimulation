class AnalyzeServiceImpl:

    def __init__(self, simulation_context):
        self.reception_queue_history = simulation_context.reception_queue_history
        self.rooms_queue_history = simulation_context.rooms_queue_history
        self.simulation_matrix = simulation_context.simulation_matrix

    def run(self):
        average_time_spent_in_system = self.calculate_average_time()
        print(f"average_time_spent_in_system = {average_time_spent_in_system}")
        average_corona_time_spent_in_system = self.calculate_average_time(patient_type='corona')
        print(f"average_corona_time_spent_in_system = {average_corona_time_spent_in_system}")
        average_normal_time_spent_in_system = self.calculate_average_time(patient_type='normal')
        print(f"average_normal_time_spent_in_system = {average_normal_time_spent_in_system}")
        average_waiting_time_in_queue = self.calculate_average_time(req='time_waited_in_queue')
        print(f"average_waiting_time_in_queue = {average_waiting_time_in_queue}")
        average_corona_waiting_time_in_queue = self.calculate_average_time(patient_type='corona',
                                                                           req='time_waited_in_queue')
        print(f"average_corona_waiting_time_in_queue = {average_corona_waiting_time_in_queue}")
        average_normal_waiting_time_in_queue = self.calculate_average_time(patient_type='normal',
                                                                           req='time_waited_in_queue')
        print(f"average_normal_waiting_time_in_queue = {average_normal_waiting_time_in_queue}")
        number_of_leaved_patients = self.calculate_number_of_leaved_patients()
        print(f"number_of_leaved_patients = {number_of_leaved_patients}")
        average_reception_queue_length = average(self.reception_queue_history)
        print(f"average_reception_queue_length = {average_reception_queue_length}")
        average_first_room_queue_length = average(self.rooms_queue_history[0])
        print(f"average_first_room_queue_length = {average_first_room_queue_length}")
        average_second_room_queue_length = average(self.rooms_queue_history[1])
        print(f"average_second_room_queue_length = {average_second_room_queue_length}")

    def calculate_average_time(self, patient_type='all', req='time_spent_in_system'):
        if patient_type == 'corona':
            return sum([patient[req] for patient in self.simulation_matrix if patient['type'] == 'corona']) / len(
                self.simulation_matrix)
        elif patient_type == 'normal':
            return sum([patient[req] for patient in self.simulation_matrix if patient['type'] == 'normal']) / len(
                self.simulation_matrix)
        else:
            return sum([patient[req] for patient in self.simulation_matrix]) / len(self.simulation_matrix)

    def calculate_number_of_leaved_patients(self):
        return sum([1 for patient in self.simulation_matrix if patient['did_leave']])


def average(items):
    if len(items) == 0:
        return 0
    return sum(items) / len(items)
