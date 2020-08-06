from controller.SimulationController import SimulationController
import time


if __name__ == '__main__':
    start = time.time()
    simulation_controller = SimulationController(number_of_patients=1000)
    simulation_controller.start_process()
    end = time.time()
    print(f'simulation_took: {end-start}')


