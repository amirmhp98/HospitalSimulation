from model.dto.SimulationContext import SimulationContext


class SimulationFlowServiceImpl:

    def __init__(self):
        self.time = 0

    def runSimulation(self, simulationContext: SimulationContext):

        simulationFinished = False
        timer = 0

        matrix = simulationContext.simulationMatrix

        while not simulationFinished:
            # todo implement
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
            pass
        return matrix
