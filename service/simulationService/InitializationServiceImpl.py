from model.dto.SimulationContext import SimulationContext
from model.Hospital import Hospital
from model.Worker import Receptionist, Doctor
from model.Room import Room
from service.randomizationService import ExponentialDistribution, PoissonDistribution


class InitializationServiceImpl:
    def __init__(self, simulation_parameters, number_of_patients):
        self.number_of_rooms = simulation_parameters[0]
        self.patient_arrival_rate = simulation_parameters[1]
        self.average_patience = simulation_parameters[2]
        self.reception_service_rate = simulation_parameters[3]
        self.doctors_service_rate = simulation_parameters[4]
        self.number_of_patients = number_of_patients

    def initialize_simulation(self):
        # todo pass needed params, signatures need to be changed
        hospital = self.initialize_hospital()
        matrix = self.initialize_matrix()
        context = SimulationContext(hospital, matrix, self.average_patience)
        return context

    def initialize_hospital(self):
        # todo implement
        receptionist_distribution = PoissonDistribution(self.reception_service_rate)
        receptionist = Receptionist(receptionist_distribution)

        rooms = []
        for room_number in range(self.number_of_rooms):
            room_doctors = []
            for doctor_service_rate in self.doctors_service_rate[room_number]:
                doctor_distribution = ExponentialDistribution(doctor_service_rate)
                doctor = Doctor(doctor_distribution)
                room_doctors.append(doctor)

            room = Room(room_doctors)
            rooms.append(room)

        hospital = Hospital(receptionist, rooms)
        return hospital

    def initialize_matrix(self):
        # todo implement
        return
