from controller.SimulationController import SimulationController


if __name__ == '__main__':
    simulation_controller = SimulationController(number_of_patients=10)
    simulation_controller.start_process()


