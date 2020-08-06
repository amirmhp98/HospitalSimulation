from model.Hospital import Hospital
from model.Room import Room

from queue import Queue
from heapq import heapify, heappush, heappop

from model.dto.SimulationContext import SimulationContext
from model.Worker import Receptionist, Doctor


class SimulationFlowServiceImpl:

    def __init__(self):
        self.timer = 0
        self.current_patient_index = 0

    def run_simulation(self, simulation_context: SimulationContext):
        matrix = simulation_context.simulation_matrix
        hospital = simulation_context.hospital
        event_list = []
        reception_queue = Queue()  # this queue only holds the IDs of patients not the actual object
        # self.initialize_event_list(simulation_context, event_list)

        next_report_time = 0
        while not self.check_simulation_finish(matrix, reception_queue, simulation_context.hospital.rooms):
            """
            while flow:
            1- go through event list while event.time == timer and make your own small *current* event list
            2- go through small *current* event list and:
                2A- if receptionist is becoming free:
                    2A.1- get duration rand
                    2A.2- register its next free time event in queue
                    2A.3- move it's pointer to next patient (next matrix row, next Cid)
                    2A.4- receipt it, assign it to less crowded room and add it to its proper queue
                        2A.4.1- if the room has free doctor, pick first free and #assign_it_to_the_doctor
                    2A.5- fill the matrix (rec.time, rec.dur, room, ...)
                2B- if doctor is becoming free:
                    2B.1- go through corona(then normal) queue and check if they frustrated, until the first still waiting patient
                    2B.2- register doctor as room's free doctor
                    2B.3- if there is patient in queue:
                        2B.3.1- fetch proper patient
                        2B.3.2- get duration rand
                        2B.3.3- register its next free time event in queue
                        2B.3.4- fill the matrix
            3- check event list size
                3A- if it is empty, simulationFinished = true
                3B- else set the timer to next soonest event
            """
            next_report_time = self.progress_report(progress_report_interval=100000, next_report_time=next_report_time)
            self.timer = self.next_soonest_event(event_list=event_list, matrix=matrix)  # step 3 done
            self.insert_patients(reception_queue, matrix)
            current_event_list = self.build_current_event_list(event_list)  # step 1 done
            if hospital.receptionist.status == 'free':
                self.handle_receptionist_event(hospital.receptionist, event_list, hospital, matrix, reception_queue,
                                               simulation_context.patience)
            for room in hospital.rooms:
                if room.normal_queue.qsize() + room.corona_queue.qsize() > 0:
                    for doctor in room.doctors:
                        if doctor.status == 'free':
                            current_event_list.append((0, doctor))
            # print('hi')
            for _, event in current_event_list:  # step 2:
                if isinstance(event, Receptionist):
                    # 2A
                    self.handle_receptionist_event(event, event_list, hospital, matrix, reception_queue,
                                                   simulation_context.patience)

                elif isinstance(event, Doctor):
                    # 2B
                    self.handle_doctor_event(event, event_list, simulation_context)

            self.record_queue_length(simulation_context, reception_queue.qsize())
        return simulation_context

    def progress_report(self, progress_report_interval, next_report_time):
        if self.current_patient_index > next_report_time:
            next_report_time += progress_report_interval
            print(f"progress_report: last_entered_patient:{self.current_patient_index}, "
                  f"time:{self.timer}")
        return next_report_time

    def handle_doctor_event(self, event, event_list, simulation_context):
        corona_queue = event.room.corona_queue
        normal_queue = event.room.normal_queue
        # print(corona_queue.qsize(), normal_queue.qsize())
        patient = self.get_patient_from_queue(corona_queue, simulation_context.patience)
        if not patient:
            patient = self.get_patient_from_queue(normal_queue, simulation_context.patience)
        if patient:
            duration = event.get_next_random_duration()
            event.status = 'busy'
            heappush(event_list, (self.timer + duration, event))
            patient['leave_time'] = self.timer + duration
            patient['time_waited_in_queue'] = self.timer - patient['arrival_time']
            patient['time_spent_in_system'] = patient['leave_time'] - patient['arrival_time']
        else:
            event.status = 'free'
            # heappush(event_list, (self.timer + 1, event))

    def handle_receptionist_event(self, event, event_list, hospital, matrix, reception_queue, patience):
        if reception_queue.qsize() > 0:
            current_patient = self.get_patient_from_queue(reception_queue, patience)
            if current_patient:
                event.status = 'busy'
                duration = event.get_next_random_duration()  # 2A.1
                heappush(event_list, (self.timer + duration, event))  # 2A.2
                self.assign_to_room(patient=current_patient, hospital=hospital)  # 2A.4
                self.record_waiting_time_for_patient(current_patient)  # 2A.5
            else:
                event.status = 'free'
        else:
            event.status = 'free'
            # heappush(event_list, (self.timer + 1, event))

    def get_patient_from_queue(self, queue: Queue, patience):
        if queue.qsize() > 0:
            front_patient = queue.get()
            if self.timer - front_patient['arrival_time'] > patience:
                front_patient['leave_time'] = front_patient['arrival_time'] + patience
                front_patient['time_waited_in_queue'] = patience
                front_patient['time_spent_in_system'] = front_patient['leave_time'] - front_patient['arrival_time']
                front_patient['did_leave'] = True
                # print(f"patient left the system, patient={front_patient}")  # FIXME: remove

                return self.get_patient_from_queue(queue, patience)
            else:
                return front_patient

        return False

    def check_simulation_finish(self, matrix, reception_queue, rooms):
        if self.current_patient_index == len(matrix) and not reception_queue.qsize() and self.rooms_are_idle(rooms):
            return True
        return False

    def build_current_event_list(self, event_list):
        current_event_list = []
        while event_list and event_list[0][0] == self.timer:
            current_event_list.append(heappop(event_list))
        return current_event_list[::-1]  # so receptionist always come before doctors

    def insert_patients(self, reception_queue, matrix):
        while self.current_patient_index < len(matrix) and matrix[self.current_patient_index][
            'arrival_time'] <= self.timer:
            reception_queue.put(matrix[self.current_patient_index])
            self.current_patient_index += 1

    def initialize_event_list(self, simulation_context, event_list):
        receptionist = simulation_context.hospital.receptionist
        heappush(event_list, (0, receptionist))

        for room in simulation_context.hospital.rooms:
            for doctor in room.doctors:
                heappush(event_list, (0, doctor))

    def next_soonest_event(self, event_list, matrix):
        if event_list:
            timer = event_list[0][0]
        else:
            timer = matrix[self.current_patient_index]['arrival_time']
        return timer

    def assign_to_room(self, patient, hospital: Hospital):
        least_crowded_room = sorted(hospital.rooms,
                                    key=lambda room: room.corona_queue.qsize() + room.normal_queue.qsize())[0]
        if patient['type'] == 'corona':
            least_crowded_room.corona_queue.put(patient)
        else:
            least_crowded_room.normal_queue.put(patient)

    def record_queue_length(self, simulation_context: SimulationContext, current_reception_queue_length):
        simulation_context.reception_queue_history[self.timer] = current_reception_queue_length
        for index, room in enumerate(simulation_context.hospital.rooms):
            simulation_context.rooms_queue_history[index][
                self.timer] = room.corona_queue.qsize() + room.normal_queue.qsize()

    def record_waiting_time_for_patient(self, patient):
        arrival_time = patient['arrival_time']
        patient['time_waited_in_queue'] += self.timer - arrival_time

    def rooms_are_idle(self, rooms):
        for room in rooms:
            for doctor in room.doctors:
                if doctor.status == 'busy':
                    return False
        return True
