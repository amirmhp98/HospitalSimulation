class InputServiceImpl:

    def get_inputs(self):
        # M, landa, alpha, mu = map(float, input().split())
        number_of_rooms, patient_arrival_rate, average_patience, reception_service_rate, = map(float, input().split())
        number_of_rooms = int(number_of_rooms)
        doctors_service_rate = []
        for room_mu_s in range(number_of_rooms):
            doctors_service_rate.append(list(map(float, input().split())))
        return number_of_rooms, patient_arrival_rate, average_patience, reception_service_rate, doctors_service_rate
